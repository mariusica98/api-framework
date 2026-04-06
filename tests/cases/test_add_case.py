import pytest
import requests
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

class TestCreateCaseFlow:

    @allure.feature("Case Management")
    @allure.title("Create Case successfully")
    def test_create_case(self, case_helper):

        case_folder = None
        case_id = None
        try:
            # --- Create case  ---
            with allure.step("Creating a new case"):
                case_folder = case_helper.create_case(CREATE_CASE_INPUT_1)
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
                first_case_folder = case_helper.create_case(CREATE_CASE_INPUT_1)
                first_case_id = first_case_folder["id"]

            # --- Attempt to create second case with same name ---
            with allure.step("Creating a second case with the same name"):
                second_case_folder = case_helper.create_case(CREATE_CASE_INPUT_1)

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
    
    @allure.feature("Case Management")
    @allure.title("Create Case with error - empty case status")
    def test_create_case_empty_status(self, case_helper):

        error_response = None
        input_data = CREATE_CASE_EMPTY_STATUS_INPUT.copy()
        input_data["status"] = ""
        try:
            # --- Create case with empty status ---
            with allure.step("Creating a case with empty status"):
                try:
                    response = case_helper.create_case(input_data)
                except requests.exceptions.HTTPError as e:
                    response_json = e.response.json()
                    # Create a structured error response from the GraphQL error
                    error_response = GraphQLErrorResponse(
                        errors=[GraphQLError(
                            message=err.get("message"),
                            extensions=GraphQLErrorExtensions(
                                code=err.get("extensions", {}).get("code")
                            )
                        ) for err in response_json.get("errors", [])],
                        data=response_json.get("data")
                    )
                else:
                    if response.get("status") == "error":
                        error_response = GraphQLErrorResponse(**response)

             # --- Assertions for case with empty status ---
            with allure.step("Verifying errors for case with empty status"):
                assert error_response is not None, "Expected an error response when status is empty"
                assert len(error_response.errors) > 0, "Expected at least one error"
                error = error_response.errors[0]
                assert "caseStatus" in error.message, f"Expected 'caseStatus' in error message, got: {error.message!r}"
                assert error.extensions.code == "INVALID_VALUE", f"Expected code 'INVALID_VALUE', got: {error.extensions.code!r}"

        finally:
            # --- Verify that no case was created ---
            with allure.step("Verifying that no case was created"):
                assert error_response.data is None or \
                    error_response.data.get("createConversationSafeFolder") is None, \
                    "Expected no case to be created when status is empty"
    
    @allure.feature("Case Management")
    @allure.title("Create Case with error - empty initial content status")
    def test_create_case_empty_initial_content_status(self, case_helper):

        error_response = None
        input_data = CREATE_CASE_EMPTY_INITIAL_CASE_CONTENT_STATUS_INPUT.copy()
        input_data["contentStatus"] = ""
        try:
            # --- Create case with empty initial content status ---
            with allure.step("Creating a case with empty initial content status"):
                try:
                    response = case_helper.create_case(input_data)
                except requests.exceptions.HTTPError as e:
                    response_json = e.response.json()
                    # Create a structured error response from the GraphQL error
                    error_response = GraphQLErrorResponse(
                        errors=[GraphQLError(
                            message=err.get("message"),
                            extensions=GraphQLErrorExtensions(
                                code=err.get("extensions", {}).get("code")
                            )
                        ) for err in response_json.get("errors", [])],
                        data=response_json.get("data")
                    )
                else:
                    if response.get("status") == "error":
                        error_response = GraphQLErrorResponse(**response)

            # --- Assertions for case with empty initial content status ---
            with allure.step("Verifying errors for case with empty initial content status"):
                assert error_response is not None, "Expected an error response when initial content status is empty"
                assert len(error_response.errors) > 0, "Expected at least one error"
                error = error_response.errors[0]
                assert "contentStatus" in error.message, f"Expected 'contentStatus' in error message, got: {error.message!r}"
                assert error.extensions.code == "INVALID_VALUE", f"Expected code 'INVALID_VALUE', got: {error.extensions.code!r}"

        finally:
            # --- Verify that no case was created ---
            with allure.step("Verifying that no case was created"):
                assert error_response.data is None or \
                    error_response.data.get("createConversationSafeFolder") is None, \
                    "Expected no case to be created when initial content status is empty"
