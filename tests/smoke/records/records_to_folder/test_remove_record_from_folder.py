import pytest
import allure
from config.graphql_client import *
from utils.helper.conversation_safe_folder_helper.folder_helper import FolderHelper
from utils.helper.record_helper import *
from utils.test_data import *
from variables.conversation_safe_variables.folder_variables import DEFAULT_FOLDER_INPUT_PARAMS, build_create_folder_input
from variables.record_variables import *

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()

@pytest.fixture(scope="module")
def folder_helper(client):
    return FolderHelper(client)

@pytest.fixture(scope="module")
def record_helper(client):
    return RecordHelper(client)

class TestRemoveRecordFromFolderFlow:

    @allure.feature("Records")
    @allure.title("Remove record from folder successfully: Record page (bulk operation)")
    def test_remove_record_from_folder_from_record_page(self, folder_helper, record_helper):

        folder_id = None
        try:
            # --- Create a new folder ---
            create_input = build_create_folder_input(**DEFAULT_FOLDER_INPUT_PARAMS)
            with allure.step("Creating a new folder"):
                folder = folder_helper.create_folder(create_input)
                folder_id = folder["id"]

            # --- Input for adding record to folder ---
            add_record_params = DEFAULT_ADD_RECORD_TO_FOLDER_PARAMS.copy()
            add_record_params.update({
                "user_id": TEST_USER_ID,
                "tenant_id": TEST_TENANT_ID,
                "conversations": [{"conversationId": TEST_RECORD_ID}],
                "csf_id": folder_id
            })

            add_record_input = build_add_record_to_folder_input(**add_record_params)

            # --- Add record to folder ---
            with allure.step("Adding record to folder"):
                record_helper.add_record_to_csf(add_record_input)

            # --- Input for remove record from folder ---
            remove_input = build_remove_record_folder_input(
                conversation_ids=[TEST_RECORD_ID],
                folder_id=folder_id 
            )

            # --- Remove record from folder from records bulk operation ---
            with allure.step("Removing record from folder"):
                response = record_helper.remove_record_from_folder(remove_input)

            # --- Assertions for remove record from folder ---
            with allure.step("Verifying remove record from folder response"):
                assert response["status"] == "ok"

        finally:
            # --- Cleanup ---
            with allure.step("Deleting the folder"):
                if folder_id:
                    folder_helper.delete_folder_by_id(folder_id)
    
    # --- The remove record from Folder to CSF page test is not necessary because it uses the same create/update folder endpoint