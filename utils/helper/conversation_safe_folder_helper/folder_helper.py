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