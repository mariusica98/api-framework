import pytest
import allure
from utils.case_helper import CaseHelper
from variables.case_variables import *
from config.graphql_client_no_token import GraphQLClientNoToken  

@pytest.fixture(scope="module")
def client_no_token():
    # Use GraphQL client with no token for security tests
    return GraphQLClientNoToken()

@pytest.fixture(scope="module")
def case_helper(client_no_token):
    # CaseHeler use client with no token
    return CaseHelper(client_no_token)

class TestCaseSecurity:

    @allure.feature("Case Management")
    @allure.title("Security Test: Create Case without Token")
    def test_create_case_no_token(self, client_no_token):

        # --- Input for creating a case ---
        create_input = build_create_case_input(**DEFAULT_CASE_INPUT_PARAMS)

        # --- Attempt to create a case without auth token ---
        with allure.step("Attempt to create a case without auth token"):
            response = client_no_token.execute("createCase", {"input": create_input})

        # --- Asserts for rejected requests ---
        with allure.step("Verify request is rejected with 401"):
            assert response.status_code == 401, f"Expected status 401, got {response.status_code}"

        # --- Asserts for error message ---
        with allure.step("Verify error message"):
            body = response.text
            assert "Unauthorized" in body, f"Expected 'Unauthorized' in response, got: {body}"
            assert "Missing bearer token" in body, f"Expected 'Missing bearer token' in response, got: {body}"
    
    @allure.feature("Case Management")
    @allure.title("Security Test: Update Case without Token")
    def test_update_case_no_token(self, client_no_token):

        # --- Input for updating a case ---
        update_input = build_update_case_input(
            name=TEST_CASE_NAME_UPDATED,
            description=TEST_CASE_DESCRIPTION_UPDATED,
            case_status=TEST_CASE_STATUS_IN_PROGRESS,
            content_status=TEST_CASE_CONTENT_STATUS_ESCALED,
            content_risk_rating=TEST_CASE_RISK_RATING_ADHERANCE,
            user_id=TEST_USER_ID,
            tenant_id=TEST_TENANT_ID
        )

        # --- Attempt to update a case without auth token ---
        with allure.step("Attempt to update case without auth token"):
            response = client_no_token.execute(
                "updateCase",
                {
                    "id": TEST_INVALID_CASE_ID,
                    "input": update_input
                }
            )

        # --- Asserts for rejected requests ---
        with allure.step("Verify request is rejected with 401"):
            assert response.status_code == 401

        # --- Asserts for error message ---
        with allure.step("Verify error message is Unauthorized"):
            assert "Unauthorized" in response.text
            assert "Missing bearer token" in response.text
    
    @allure.feature("Case Management")
    @allure.title("Security Test: Delete Case without Token")
    def test_delete_case_no_token(self, client_no_token):

        # --- Input for deleting a case ---
        delete_input = build_delete_case_input(case_id=TEST_INVALID_CASE_ID)

        # --- Attempt to delete a case without auth token ---
        with allure.step("Attempt to delete case without auth token"):
            response = client_no_token.execute(
                "deleteCase",
                {
                    "conversationSafeFolder": delete_input["conversationSafeFolder"]
                }
            )

        # --- Asserts for rejected requests ---
        with allure.step("Verify request is rejected with 401"):
            assert response.status_code == 401

        # --- Asserts for error message ---
        with allure.step("Verify error message is Unauthorized"):
            assert "Unauthorized" in response.text
            assert "Missing bearer token" in response.text
    
    @allure.feature("Case Management")
    @allure.title("Security Test: Get All Cases without Token")
    def test_get_all_cases_no_token(self, client_no_token):

            # --- Attempt to get all cases without auth token ---
        with allure.step("Attempt to fetch all cases without auth token"):
            response = client_no_token.execute(
                "getAllCases",
                {
                    "filter": "AllItems"
                }
            )

        # --- Asserts for rejected requests ---
        with allure.step("Verify request is rejected with 401"):
            assert response.status_code == 401

        # --- Asserts for error message ---
        with allure.step("Verify unauthorized error message"):
            assert "Unauthorized" in response.text
            assert "Missing bearer token" in response.text