import pytest
import allure

from config.graphql_client import GraphQLClient
from utils.helper.record_helper import RecordHelper
from utils.test_data import TEST_RECORD_DURATION, TEST_RECORD_END_TIME, TEST_RECORD_EXPIRTION_DATE, TEST_RECORD_ID, TEST_RECORD_START_TIME, TEST_TENANT_ID
from variables.record_variables import build_generate_jwt_token_input, build_get_entry_with_jwt_input

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()

@pytest.fixture(scope="module")
def record_helper(client):
    return RecordHelper(client)

class TestShareRecordFlow:

    @allure.feature("Records")
    @allure.title("Check share record with success")
    def test_share_record(self, record_helper):

        # --- Generate JWT token to be used for share record ---
        with allure.step("Generate JWT token for a call"):
            token_input = build_generate_jwt_token_input(
                conversation_id=TEST_RECORD_ID,
                tenant_id=TEST_TENANT_ID,
                expiration_date=TEST_RECORD_EXPIRTION_DATE
            )

            jwt_token = record_helper.generate_jwt_token_for_call(token_input)
        
        # --- Assertions for generated token ---
        with allure.step("Verify the generated token"):
            assert jwt_token is not None
            assert jwt_token != ""
        
        # --- Input for share record ---
        with allure.step("Build input for getEntryWithJWT"):
            entry_input = build_get_entry_with_jwt_input(
                jwt_token=jwt_token
            )

        # --- Execute share record ---
        with allure.step("Execute getEntryWithJWT query"):
            response = record_helper.get_entry_with_jwt(entry_input)
         
        # --- Assertions for shared record ---
        with allure.step("Validate record response"):
            assert response is not None
            assert response["conversationId"] == TEST_RECORD_ID
            assert response["duration"] == TEST_RECORD_DURATION
            assert response["callStartMs"] == TEST_RECORD_START_TIME
            assert response["callEndMs"] ==TEST_RECORD_END_TIME

 