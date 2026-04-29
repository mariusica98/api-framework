from queries.user_queries import CREATE_USER_MUTATION, UPDATE_USER_MUTATION


class UserHelper:
    """
    Helper class for User GraphQL operations
    """

    def __init__(self, client):
        self.client = client

    def create_user(self, input_data):
        response = self.client.execute(CREATE_USER_MUTATION, input_data)

        result = response["data"]["createUser"]

        # FIX: API returnează listă uneori
        if isinstance(result, list):
            return result[0]

        return result

    def update_user(self, input_data):
        """
        Update user
        """
        response = self.client.execute(UPDATE_USER_MUTATION, input_data)
        return response["data"]["updateUser"]