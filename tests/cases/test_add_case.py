import pytest
from config.graphql_client import GraphQLClient
from utils.case_helper import CaseHelper
from variables.case_variables import CREATE_CASE_INPUT
import allure

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()

@pytest.fixture(scope="module")
def case_helper(client):
    return CaseHelper(client)

class TestCreateCaseFlow:

    @allure.feature("Case Management")
    @allure.title("Create Case successfully")
    def test_create_case(self, case_helper):

        case_folder = None
        case_id = None
        try:
            # --- Create case  ---
            with allure.step("Creating a new case"):
                case_folder = case_helper.create_case(CREATE_CASE_INPUT)
                case_id = case_folder["id"]

            # --- Assertions for create ---
            with allure.step("Verifying created case"):
                assert isinstance(case_id, str) and case_id != "", \
                    f"Expected non-empty string for id, got: {case_id!r}"
                assert case_folder["status"] == "ok", \
                    f"Expected status 'ok', got: {case_folder['status']!r}"
                assert case_folder["text"] == "", \
                    f"Expected text to be empty string, got: {case_folder['text']!r}"

        finally:
            # Cleanup
            with allure.step("Deleting the case"):
                if case_id:
                    case_helper.delete_case_by_id(case_id)
