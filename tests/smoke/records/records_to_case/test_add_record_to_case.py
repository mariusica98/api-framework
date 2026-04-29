import pytest
import allure
from config.graphql_client import *
from utils.helper.conversation_safe_folder_helper.case_helper import *
from utils.helper.record_helper import *
from variables.conversation_safe_variables.case_variables import *
from utils.test_data import *
from variables.record_variables import DEFAULT_ADD_RECORD_CASE_PARAMS, build_add_record_case_input, build_add_record_to_case_bulk_input

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()

@pytest.fixture(scope="module")
def case_helper(client):
    return CaseHelper(client)

@pytest.fixture(scope="module")
def record_helper(client):
    return RecordHelper(client)

@pytest.fixture
def cleanup_context(case_helper):
    context = {
        "case_id": None
    }

    yield context

    with allure.step("Cleanup: deleting created case"):
        if context["case_id"]:
            case_helper.delete_case_by_id(context["case_id"])

class TestAddRecordToCaseFlow:
    
    @allure.feature("Records")
    @allure.title("Add record to case successfully: CSF page")
    def test_add_record_to_case_from_csf_page(self, case_helper, record_helper, cleanup_context):

        # --- Create a new case ---
        create_input = build_create_case_input(**DEFAULT_CASE_INPUT_PARAMS)
        with allure.step("Creating a new case"):
            case_folder = case_helper.create_case(create_input)
            case_id = case_folder["id"]
            cleanup_context["case_id"] = case_id

        # --- Create input for add record to case ---
        add_record_params = DEFAULT_ADD_RECORD_CASE_PARAMS.copy()
        add_record_params.update({
            "user_id": TEST_USER_ID,
            "tenant_id": TEST_TENANT_ID,
            "conversations": [{"conversationId": TEST_RECORD_ID}],
            "case_id": case_id
        })

        add_record_input = build_add_record_case_input(**add_record_params)

        # --- Add record to case from case window ---
        with allure.step("Adding record to case"):
            response_folder = record_helper.add_record_to_csf(add_record_input)

        # --- Assertions for add record to case ---
        with allure.step("Verifying add record to case response"):
            assert isinstance(response_folder["id"], str) and response_folder["id"] != ""
            assert response_folder["status"] == "ok"
            assert response_folder["text"] == ""
    
    @allure.feature("Records")
    @allure.title("Add record to case successfully: Record page (bulk operation)")
    def test_add_record_to_case_from_record_page(self, case_helper, record_helper, cleanup_context):

        # --- Create a new case ---
        create_input = build_create_case_input(**DEFAULT_CASE_INPUT_PARAMS)
        with allure.step("Creating a new case"):
            case_folder = case_helper.create_case(create_input)
            case_id = case_folder["id"]
            cleanup_context["case_id"] = case_id

        # --- Build bulk add record to case input ---
        add_input = build_add_record_to_case_bulk_input(
            conversation_ids=[TEST_RECORD_ID],
            case_id=case_id,
            risk_rating=TEST_CASE_RISK_RATING_INFORMATION
        )

        # --- Add record to case from record page (bulk) ---
        with allure.step("Adding record to case (bulk operation)"):
            response = record_helper.add_record_to_case_bulk(add_input)

        # --- Assertions ---
        with allure.step("Verifying add record to case response"):
            assert response["status"] == "ok"