import pytest
import allure
from config.graphql_client import GraphQLClient
from utils.helper.conversation_safe_folder_helper.folder_helper import FolderHelper
from variables.conversation_safe_variables.folder_variables import *
from utils.test_data import *


@pytest.fixture(scope="module")
def client():
    return GraphQLClient()


@pytest.fixture(scope="module")
def folder_helper(client):
    return FolderHelper(client)


class TestCreateFolderFlow:

    @allure.feature("Folder Management")
    @allure.title("Create Folder successfully")
    def test_create_folder(self, folder_helper):

        folder = None
        folder_id = None
        try:
            # --- Prepare input data ---
            create_input = build_create_folder_input(**DEFAULT_FOLDER_INPUT_PARAMS)

            # --- Create folder ---
            with allure.step("Creating a new folder"):
                folder = folder_helper.create_folder(create_input)
                folder_id = folder["id"]

            # --- Assertions for created folder ---
            with allure.step("Verifying created folder"):
                assert isinstance(folder_id, str) and folder_id != "", \
                    f"Expected non-empty string for id, got: {folder_id!r}"
                assert folder["status"] == "ok", \
                    f"Expected status 'ok', got: {folder['status']!r}"
                assert folder["text"] == "", \
                    f"Expected text to be empty string, got: {folder['text']!r}"

        finally:
            # --- Cleanup (if needed later when delete exists) ---
            with allure.step("Cleanup folder"):
                pass