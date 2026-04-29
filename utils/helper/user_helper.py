from queries.user_queries import CREATE_USER_MUTATION, DELETE_USER_MUTATION, GET_CONFIG_DATA_QUERY, UPDATE_USER_MUTATION
from variables.user_variables import DEFAULT_AUTH


class UserHelper:
    """
    Helper class for User GraphQL operations
    """

    def __init__(self, client):
        self.client = client

    def create_user(self, input_data):
        """
        Create user
        """
        response = self.client.execute(CREATE_USER_MUTATION, input_data)

        result = response["data"]["createUser"]

        if isinstance(result, list):
            return result[0]

        return result

    def update_user(self, input_data):
        """
        Update user
        """
        response = self.client.execute(UPDATE_USER_MUTATION, input_data)
        return response["data"]["updateUser"]

    def delete_user(self, input_data):
        """
        Delete user by id
        """
        response = self.client.execute(DELETE_USER_MUTATION, input_data)

        result = response["data"]["deleteUser"]

        if result is None:
            raise Exception(f"Delete user failed: {response}")

        return result

    def get_users(self):
        """
        Get all users from tenant
        """
        response = self.client.execute(
            GET_CONFIG_DATA_QUERY,
            {"auth": DEFAULT_AUTH}
        )

        return response["data"]["getConfigData"]["userdata"]

    def find_user_by_name(self, name):
            """
            Find user by name
            """
            users = self.get_users()

            return next((u for u in users if u["name"] == name), None)