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


    @allure.feature("Case Management")
    @allure.title("Create Case with error - duplicate name")
    def test_create_duplicate_case(self, case_helper):

        first_case_folder = None
        second_case_folder = None
        first_case_id = None
        try:
            # --- Create first case ---
            with allure.step("Creating the first case"):
                first_case_folder = case_helper.create_case(CREATE_CASE_INPUT)
                first_case_id = first_case_folder["id"]

            # --- Attempt to create second case with same name ---
            with allure.step("Creating a second case with the same name"):
                second_case_folder = case_helper.create_case(CREATE_CASE_INPUT)

            # --- Assertions for duplicate case ---
            with allure.step("Verifying errors for duplicate case"):
                assert second_case_folder["status"] == "error", \
                    f"Expected status 'error' for duplicate case, got: {second_case_folder['status']!r}"
                assert second_case_folder["text"] == "nameDuplicatedError", \
                    f"Expected text 'nameDuplicatedError', got: {second_case_folder['text']!r}"
                assert second_case_folder["id"] == "", \
                    f"Expected empty ID for duplicate case, got: {second_case_folder['id']!r}"

        finally:
            # Cleanup
            with allure.step("Deleting the first case"):
                if first_case_id:
                    case_helper.delete_case_by_id(first_case_id)