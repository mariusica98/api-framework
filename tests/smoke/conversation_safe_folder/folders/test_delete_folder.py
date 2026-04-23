import pytest
import allure
from config.graphql_client import GraphQLClient
from utils.helper.conversation_safe_folder_helper.folder_helper import FolderHelper
from variables.conversation_safe_variables.folder_variables import *
from utils.test_data import *
from error_models.case_error_model import GetCsfNonExistingIdResponse


@pytest.fixture(scope="module")
def client():
    return GraphQLClient()


@pytest.fixture(scope="module")
def folder_helper(client):
    return FolderHelper(client)

class TestDeleteFolderFlow:

    @allure.feature("Conversation Safe Folder")
    @allure.title("Delete Folder successfully")
    def test_delete_folder_by_id(self, folder_helper):

        folder = None
        folder_id = None

        # --- Prepare input data for create folder---
        create_input = build_create_folder_input(**DEFAULT_FOLDER_INPUT_PARAMS)

        # --- Create folder ---
        with allure.step("Creating a new folder"):
            folder = folder_helper.create_folder(create_input)
            folder_id = folder["id"]
        
        # --- Delete the created folder ---
        with allure.step("Deleting folder"):
            delete_input = build_delete_folder_input(folder_id=folder_id)
            delete_status, delete_typename = folder_helper.delete_folder_by_id(delete_input["conversationSafeFolder"])

        # --- Assertions for delete folder ---
        with allure.step("Verifying the case was deleted"):
            assert delete_status == "ok", (
                f"Expected delete status 'ok', got: {delete_status!r}"
            )
            assert delete_typename == "MessageResponse", (
                f"Expected typename 'MessageResponse', got: {delete_typename!r}"
            )
        
        # --- Verify the folder is no longer retrievable ---
        with allure.step("Verifying the folder cannot be retrieved after deletion"):
            folder_data = folder_helper.get_conversation_safe_folder_by_id(folder_id)
            actual_folder = GetCsfNonExistingIdResponse(**folder_data)

        # --- Expected empty/error folder ---
        expected_folder = GetCsfNonExistingIdResponse(
            id=None,
            name=None,
            description=None,
            supervisors=[],
            conversations=[],
            allowedInPolicy=False,
            allowedToEditFlagAllowedInPolicy=False,
            isCaseManagement=False
        )

        # --- Assertions for get folder by non-existent ID ---
        with allure.step("Verifying response fields for non-existent folder"):
            assert actual_folder == expected_folder