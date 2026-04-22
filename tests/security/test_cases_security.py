import pytest
import allure
from utils.helper.conversation_safe_folder_helper.case_helper import CaseHelper
from variables.conversation_safe_variables.case_variables import *
from config.graphql_client_invalid_token import GraphQLClientNoToken

@pytest.fixture(scope="function")
def client():
    return GraphQLClientNoToken()

@pytest.fixture(scope="function")
def case_helper(client):
    return CaseHelper(client)

@allure.feature("Case Management")
@allure.story("Security - Authentication Failures")
class TestCaseSecurity:

    # --- NO TOKEN ---
    @allure.feature("Case Management")
    @allure.title("Security Test: Create Case without Token")
    def test_create_case_no_token(self, client):

        #--- Use no token ---
        client.use_no_token()

        # --- Input data for create case ---
        create_input = build_create_case_input(**DEFAULT_CASE_INPUT_PARAMS)

        #--- Attempt to create a case without auth token ---
        with allure.step("Attempt to create a case without auth token"):
            response = client.execute("createCase", {"input": create_input})

        # --- Assertion for no token ---
        with allure.step("Verify that the response indicates unauthorized access"):
            assert response.status_code == 401
            assert "Unauthorized" in response.text
            assert "Missing bearer token" in response.text

    @allure.feature("Case Management")
    @allure.title("Security Test: Update Case without Token")
    def test_update_case_no_token(self, client):

        #-- Use no token ---
        client.use_no_token()

        #-- Input data for update case ---
        update_input = build_update_case_input(
            name=TEST_CASE_NAME_UPDATED,
            description=TEST_CASE_DESCRIPTION_UPDATED,
            case_status=TEST_CASE_STATUS_IN_PROGRESS,
            content_status=TEST_CASE_CONTENT_STATUS_ESCALED,
            content_risk_rating=TEST_CASE_RISK_RATING_ADHERANCE,
            user_id=TEST_USER_ID,
            tenant_id=TEST_TENANT_ID
        )

        #-- Attempt to update a case without auth token ---
        with allure.step("Attempt to update a case without auth token"):
            response = client.execute("updateCase", {"id": TEST_INVALID_CASE_ID, "input": update_input})

        #-- Assertions for no token ---
        with allure.step("Verify that the response indicates unauthorized access"):
            assert response.status_code == 401
            assert "Unauthorized" in response.text
            assert "Missing bearer token" in response.text

    @allure.feature("Case Management")
    @allure.title("Security Test: Delete Case without Token")
    def test_delete_case_no_token(self, client):

        #-- Use no token ---
        client.use_no_token()

        #-- Input data for delete case ---
        delete_input = build_delete_case_input(case_id=TEST_INVALID_CASE_ID)

        #-- Attempt to delete a case without auth token ---
        with allure.step("Attempt to delete a case without auth token"):
            response = client.execute(
                "deleteCase",
                {"conversationSafeFolder": delete_input["conversationSafeFolder"]}
            )

        #-- Assertions for no token ---
        with allure.step("Verify that the response indicates unauthorized access"):
            assert response.status_code == 401
            assert "Unauthorized" in response.text
            assert "Missing bearer token" in response.text

    @allure.feature("Case Management")
    @allure.title("Security Test: Get All Cases without Token")
    def test_get_all_cases_no_token(self, client):

        #-- Use no token ---
        client.use_no_token()

        #-- Attempt to get all cases without auth token ---
        with allure.step("Attempt to get all cases without auth token"):
            response = client.execute("getAllCases", {"filter": "AllItems"})

        #-- Assertions for no token ---
        with allure.step("Verify that the response indicates unauthorized access"):
            assert response.status_code == 401
            assert "Unauthorized" in response.text
            assert "Missing bearer token" in response.text

    # --- EXPIRED TOKEN ---
    @allure.feature("Case Management")
    @allure.title("Security Test: Create Case with Expired Token")
    def test_create_case_expired_token(self, client):

        #-- Use expired token ---
        client.use_expired_token()

        #-- Input data for create case ---
        create_input = build_create_case_input(**DEFAULT_CASE_INPUT_PARAMS)

        #-- Attempt to create a case with expired auth token ---
        with allure.step("Attempt to create a case with expired auth token"):
            response = client.execute("createCase", {"input": create_input})

            #-- Assertions for expired token ---
        with allure.step("Verify that the response indicates unauthorized access due to expired token"):
            assert response.status_code == 401
            body = response.text.lower()
            assert "unauthorized" in body or "invalid" in body

    @allure.feature("Case Management")
    @allure.title("Security Test: Update Case with Expired Token")
    def test_update_case_expired_token(self, client):

        #-- Use expired token ---
        client.use_expired_token()

        #-- Input data for update case ---
        update_input = build_update_case_input(
            name=TEST_CASE_NAME_UPDATED,
            description=TEST_CASE_DESCRIPTION_UPDATED,
            case_status=TEST_CASE_STATUS_IN_PROGRESS,
            content_status=TEST_CASE_CONTENT_STATUS_ESCALED,
            content_risk_rating=TEST_CASE_RISK_RATING_ADHERANCE,
            user_id=TEST_USER_ID,
            tenant_id=TEST_TENANT_ID
        )

        #-- Attempt to update a case with expired auth token ---
        with allure.step("Attempt to update a case with expired auth token"):
            response = client.execute("updateCase", {"id": TEST_INVALID_CASE_ID, "input": update_input})

        #-- Assertions for expired token ---
        with allure.step("Verify that the response indicates unauthorized access due to expired token"):
            assert response.status_code == 401
            body = response.text.lower()
            assert "unauthorized" in body or "invalid" in body

    @allure.feature("Case Management")
    @allure.title("Security Test: Get All Cases with Expired Token")
    def test_get_all_cases_expired_token(self, client):

        #-- Use expired token ---
        client.use_expired_token()

        #-- Attempt to get all cases with expired auth token ---
        with allure.step("Attempt to get all cases with expired auth token"):
            response = client.execute("getAllCases", {"filter": "AllItems"})

        #-- Assertions for expired token ---
        with allure.step("Verify that the response indicates unauthorized access due to expired token"):
            assert response.status_code == 401
            body = response.text.lower()
            assert "unauthorized" in body or "invalid" in body
    
    @allure.feature("Case Management")
    @allure.title("Security Test: Delete Case with Expired Token")
    def test_delete_case_expired_token(self, client):

        #-- Use expired token ---
        client.use_expired_token()

        #-- Input data for delete case ---
        delete_input = build_delete_case_input(case_id=TEST_INVALID_CASE_ID)

        #-- Attempt to delete a case with expired auth token ---
        with allure.step("Attempt to delete a case with expired auth token"):
            response = client.execute(
                "deleteCase",
                {"conversationSafeFolder": delete_input["conversationSafeFolder"]}
            )

        #-- Assertions for expired token ---
        with allure.step("Verify that the response indicates unauthorized access due to expired token"):
            assert response.status_code == 401
            assert "Unauthorized" in response.text
            assert "Missing bearer token" in response.text