import pytest
import allure
from config.graphql_client import GraphQLClient
from utils.helper.record_helper import RecordHelper
from utils.helper.conversation_safe_folder_helper.folder_helper import FolderHelper
from variables.conversation_safe_variables.folder_variables import *
from utils.test_data import *
from variables.record_variables import DEFAULT_ADD_RECORD_TO_FOLDER_PARAMS, build_add_record_to_folder_bulk_input, build_add_record_to_folder_input


@pytest.fixture(scope="module")
def client():
    return GraphQLClient()

@pytest.fixture(scope="module")
def folder_helper(client):
    return FolderHelper(client)

@pytest.fixture(scope="module")
def record_helper(client):
    return RecordHelper(client)

class TestAddRecordToFolderFlow:

    @allure.feature("Conversation Safe Folder")
    @allure.title("Add Record to Folder successfully: CSF page")
    def test_add_record_to_folder_from_csf_page(self, folder_helper, record_helper):

        folder = None
        folder_id = None
        try:
            # --- Prepare input data ---
            create_input = build_create_folder_input(**DEFAULT_FOLDER_INPUT_PARAMS)

            # --- Create folder ---
            with allure.step("Creating a new folder"):
                folder = folder_helper.create_folder(create_input)
                folder_id = folder["id"]
            
            # --- Create input for add record to folder ---
            add_record_params = DEFAULT_ADD_RECORD_TO_FOLDER_PARAMS.copy()
            add_record_params.update({
                "user_id": TEST_USER_ID,
                "tenant_id": TEST_TENANT_ID,
                "conversations": [{"conversationId": TEST_RECORD_ID}],
                "csf_id": folder_id
            })

            add_record_input = build_add_record_to_folder_input(**add_record_params)

            # --- Add record to folder from folder window ---
            with allure.step("Adding record to folder"):
                response_folder = record_helper.add_record_to_csf(add_record_input)
            
            # --- Assertions for add record to folder ---
            with allure.step("Verifying add record to folder response"):
                assert isinstance(response_folder["id"], str) and response_folder["id"] != ""
                assert response_folder["status"] == "ok"
                assert response_folder["text"] == ""

        finally:
            # --- Cleanup ---
            with allure.step("Deleting the folder"):
                if folder_id:
                    folder_helper.delete_folder_by_id(folder_id)
    
    @allure.feature("Records")
    @allure.title("Add record to folder successfully: Record page (bulk operation)")
    def test_add_record_to_folder_from_record_page(self, folder_helper, record_helper):

        folder_id = None
        try:
            # --- Create folder ---
            create_input = build_create_folder_input(**DEFAULT_FOLDER_INPUT_PARAMS)
            with allure.step("Creating a new folder"):
                folder = folder_helper.create_folder(create_input)
                folder_id = folder["id"]

            # --- Build bulk add record to folder input ---
            add_input = build_add_record_to_folder_bulk_input(
                conversation_ids=[TEST_RECORD_ID],
                folder_id=folder_id
            )

            # --- Add record to folder (bulk) ---
            with allure.step("Adding record to folder (bulk operation)"):
                response = record_helper.add_record_to_folder_bulk(add_input)

            # --- Assertions ---
            with allure.step("Verifying add record to folder response"):
                assert response["status"] == "ok"

        finally:
            # --- Cleanup ---
            with allure.step("Deleting the folder"):
                if folder_id:
                    folder_helper.delete_folder_by_id(folder_id)