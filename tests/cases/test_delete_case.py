import pytest
from config.graphql_client import GraphQLClient
from models.case_error import *
from utils.case_helper import CaseHelper
from variables.case_variables import *
import allure

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
        # --- Create case ---
        with allure.step("Creating a new case to be deleted"):
            case_folder = case_helper.create_case(CREATE_CASE_INPUT)
            case_id = case_folder["id"]

        # --- Delete the case ---
        with allure.step("Deleting the created case"):
            delete_status, delete_typename = case_helper.delete_case_by_id(case_id)

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