import pytest
import allure
from utils.case_helper import CaseHelper
from variables.case_variables import DEFAULT_CASE_INPUT_PARAMS, build_create_case_input
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