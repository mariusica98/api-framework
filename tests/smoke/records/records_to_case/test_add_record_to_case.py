import pytest
import allure
from config.graphql_client import *
from utils.helper.conversation_safe_folder_helper.case_helper import *
from utils.helper.record_helper import *
from variables.conversation_safe_variables.case_variables import *
from utils.test_data import *
from variables.record_variables import DEFAULT_ADD_RECORD_CASE_PARAMS, build_add_record_case_input

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()

@pytest.fixture(scope="module")
def case_helper(client):
    return CaseHelper(client)

@pytest.fixture(scope="module")
def record_helper(client):
    return RecordHelper(client)

class TestAddRecordToCaseFlow:
    
    @allure.feature("Records")
    @allure.title("Add record to case successfully")
    def test_add_record_to_case(self, case_helper, record_helper):

        case_id = None
        try:
            # --- Create a new case ---
            create_input = build_create_case_input(**DEFAULT_CASE_INPUT_PARAMS)
            with allure.step("Creating a new case"):
                case_folder = case_helper.create_case(create_input)
                case_id = case_folder["id"]

            # --- Create input for add record to case ---
            add_record_params = DEFAULT_ADD_RECORD_CASE_PARAMS.copy()
            add_record_params.update({
                "user_id": TEST_USER_ID,
                "tenant_id": TEST_TENANT_ID,
                "conversations": [{"conversationId": TEST_RECORD_ID}],
                "case_id": case_id
            })

            add_record_input = build_add_record_case_input(**add_record_params)

            # --- Add record to case ---
            with allure.step("Adding record to case"):
                response_folder = record_helper.add_record_to_case(add_record_input)

            # --- Assertions for add record to case ---
            with allure.step("Verifying add record to case response"):
                assert isinstance(response_folder["id"], str) and response_folder["id"] != ""
                assert response_folder["status"] == "ok"
                assert response_folder["text"] == ""

        finally:
            # --- Cleanup ---
            with allure.step("Deleting the case"):
                if case_id:
                    case_helper.delete_case_by_id(case_id)