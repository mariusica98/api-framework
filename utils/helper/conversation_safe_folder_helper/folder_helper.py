from queries.conversation_safe_folder.folder_queries import *
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
        response = self.client.execute(CREATE_FOLDER_MUTATION, input_data)
        return response["data"]["createConversationSafeFolder"]

    def delete_folder_by_id(self, folder_id):
        """
        Deletes a Folder by its ID.
        """
        if not folder_id:
            return "skipped", None

        payload = build_delete_folder_input(folder_id=folder_id)
        response = self.client.execute(DELETE_FOLDER_MUTATION, payload)

        result = response["data"]["deleteConversationSafeFolder"]
        status = result["status"]
        typename = result.get("__typename")

        if status != "ok":
            raise Exception(f"Failed to delete folder {folder_id}, got status: {status}")

        return status, typename