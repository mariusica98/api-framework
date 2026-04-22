import pytest
import allure

from config.graphql_client import GraphQLClient
from utils.helper.conversation_safe_folder_helper.folder_helper import FolderHelper
from variables.conversation_safe_variables.folder_variables import DEFAULT_FOLDER_INPUT_PARAMS, build_create_folder_input

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()


@pytest.fixture(scope="module")
def folder_helper(client):
    return FolderHelper(client)


class TestGetFolderFlow:

    @allure.feature("Conversation Safe Folder")
    @allure.title("Get Folder by ID successfully")
    def test_get_folder_by_id(self, folder_helper):

        folder = None
        folder_id = None
        try:
            # --- Prepare input data for create folder ---
            create_input = build_create_folder_input(**DEFAULT_FOLDER_INPUT_PARAMS)

            # --- Create folder ---
            with allure.step("Creating a new folder"):
                folder = folder_helper.create_folder(create_input)
                folder_id = folder["id"]
                
            # --- Get folder by ID ---
            with allure.step("Get folder by ID"):
                folder_data = folder_helper.get_conversation_safe_folder_by_id(folder_id)

            # --- Assertions for retrieved folder ---
            with allure.step("Verify folder data"):
                assert folder_data["id"] == folder_id
                assert folder_data["name"] == create_input["conversationSafeFolder"]["name"]
                assert folder_data["description"] == create_input["conversationSafeFolder"]["description"]

        finally:
            # --- Cleanup ---
            with allure.step("Deleting folder"):
                if folder_id:
                    folder_helper.delete_folder_by_id(folder_id)