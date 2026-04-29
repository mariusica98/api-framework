from queries.user_queries import UPDATE_USER_MUTATION


class UserHelper:
    """
    Helper class for User GraphQL operations
    """

    def __init__(self, client):
        self.client = client

    def update_user(self, input_data):
        """
        Update user
        """
        response = self.client.execute(UPDATE_USER_MUTATION, input_data)
        return response["data"]["updateUser"]