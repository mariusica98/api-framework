from queries.conversation_safe_folder import *
from variables.conversation_safe_variables.folder_variables import *

class FolderHelper:
    """
    Helper class for managing Folders via GraphQL.
    Includes create operation.
    """
    def __init__(self, client):
        self.client = client

    def create_folder(self, input_data):
        """
        Creates a Folder with the provided input data.
        Returns the created folder object.
        """
        response = self.client.execute(UPSERT_CSF_MUTATION , input_data)
        return response["data"]["createConversationSafeFolder"]

    def delete_folder_by_id(self, folder_id):
        """
        Deletes a Folder by its ID.
        """
        if not folder_id:
            return "skipped", None

        payload = build_delete_folder_input(folder_id=folder_id)
        response = self.client.execute(DELETE_CSF_MUTATION, payload)

        result = response["data"]["deleteConversationSafeFolder"]
        status = result["status"]
        typename = result.get("__typename")

        if status != "ok":
            raise Exception(f"Failed to delete folder {folder_id}, got status: {status}")

        return status, typename

    def update_folder(self, input_data):
        response = self.client.execute(UPSERT_CSF_MUTATION , input_data)
        return response["data"]["createConversationSafeFolder"]

    def get_conversation_safe_folder_by_id(self, folder_id):
            """
            Get Conversation Safe Folder by ID
            """
            if not folder_id:
                return None

            variables = build_get_folder_by_id_input(
                folder_id=folder_id
            )

            response = self.client.execute(
                GET_CSF_BY_ID_QUERY,
                variables
            )

            return response["data"]["getConversationSafeFolder"]