import pytest
import allure
from config.graphql_client import *
from utils.helper.conversation_safe_folder_helper.case_helper import *
from variables.conversation_safe_variables.case_variables import *
from utils.test_data import *
from error_models.case_error_model import *

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()

@pytest.fixture(scope="module")
def case_helper(client):
    return CaseHelper(client)

class TestGetCaseFlow:

    @allure.feature("Case Management")
    @allure.title("Get Case by ID successfully")
    def test_get_case_by_id(self, case_helper):

        case_folder = None
        case_id = None
        try:
            #-- Prepare default case input data ---
            create_input = build_create_case_input(**DEFAULT_CASE_INPUT_PARAMS)

            #-- Create case ---
            with allure.step("Creating a new case for GET"):
                case_folder = case_helper.create_case(create_input)
                case_id = case_folder["id"]

            # --- Get case by ID ---
            with allure.step("Getting case by ID"):
                case_data = case_helper.get_case_by_id(case_id)

            # --- Assertions for get case ---
            with allure.step("Verifying case data"):
                assert case_data["id"] == case_id
                assert case_data["name"] == create_input["conversationSafeFolder"]["name"]
                assert case_data["description"] == create_input["conversationSafeFolder"]["description"]
                assert case_data["isCaseManagement"] is True

        finally:
            # --- Cleanup ---
            with allure.step("Deleting the case"):
                if case_id:
                    case_helper.delete_case_by_id(case_id)

    @allure.feature("Case Management")
    @allure.title("Get all cases successfully")
    def test_get_all_cases(self, case_helper):

        # --- Get all cases  ---
        with allure.step("Fetching all conversation safe folders"):
            all_cases = case_helper.get_all_cases(filter="AllItems")

        # --- Assertions for get all cases ---
        with allure.step("Verifying that the response is a list"):
            assert isinstance(all_cases, list), "Response should be a list"

        # --- Assertions for each case ---
        with allure.step("Verifying the structure of each case"):
            for case in all_cases:
                assert "id" in case, "Each case should have 'id'"
                assert "name" in case, "Each case should have 'name'"
                assert "description" in case, "Each case should have 'description'"
                assert "isCaseManagement" in case, "Each case should have 'isCaseManagement'"

    @allure.feature("Case Management")
    @allure.title("Get Case with error - non-existent case ID")
    def test_get_case_by_nonexisting_id(self, case_helper):

        # --- Get non-existent case ---
        with allure.step("Getting case with error - non-existent ID"):
            case_data = case_helper.get_case_by_id(TEST_INVALID_CASE_ID)
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
