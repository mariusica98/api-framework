import pytest
import allure
from config.graphql_client import *
from models.case_error import *
from utils.case_helper import *
from variables.case_variables import *
from utils.test_data import *

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()

@pytest.fixture(scope="module")
def case_helper(client):
    return CaseHelper(client)

class TestDeleteCaseFlow:

    @allure.feature("Case Management")
    @allure.title("Delete Case by id successfully")
    def test_delete_case_by_id(self, case_helper):

        case_folder = None
        case_id = None

        # --- Input data for create case ---
        create_input = build_create_case_input(
            name=TEST_CASE_NAME_1,
            description=TEST_CASE_DESCRIPTION,
            case_status=TEST_CASE_STATUS_OPEN,
            content_status=TEST_CASE_CONTENT_STATUS_NEW,
            content_risk_rating=TEST_CASE_RISK_RATING_INFORMATION,
            user_id="",
            tenant_id=""
        )
        
        # --- Create a case to be deleted ---
        with allure.step("Creating a new case to be deleted"):
            case_folder = case_helper.create_case(create_input)
            case_id = case_folder["id"]

        # --- Delete the created case ---
        with allure.step("Deleting the created case"):
            delete_input = build_delete_case_input(case_id=case_id)
            delete_status, delete_typename = case_helper.delete_case_by_id(delete_input["conversationSafeFolder"])

        # --- Assertions for delete ---
        with allure.step("Verifying the case was deleted"):
            assert delete_status == "ok", (
                f"Expected delete status 'ok', got: {delete_status!r}"
            )
            assert delete_typename == "MessageResponse", (
                f"Expected typename 'MessageResponse', got: {delete_typename!r}"
            )

        # --- Verify the case is no longer retrievable ---
        with allure.step("Verifying the case cannot be retrieved after deletion"):
            case_data = case_helper.get_case_by_id(case_id)
            actual_case = GetCaseNonExistingIdResponse(**case_data)

        # --- Expected empty/error case ---
        expected_case = GetCaseNonExistingIdResponse(
            id=None,
            name=None,
            description=None,
            supervisors=[],
            conversations=[],
            allowedInPolicy=False,
            allowedToEditFlagAllowedInPolicy=False,
            isCaseManagement=False
        )

        # --- Assertions for get case by non-existent ID ---
        with allure.step("Verifying response fields for non-existent case"):
            assert actual_case == expected_case