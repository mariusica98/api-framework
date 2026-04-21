import pytest
import allure
from config.graphql_client import *
from utils.record_helper import *
from variables.record_variables import *
from utils.test_data import *

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()

@pytest.fixture(scope="module")
def record_helper(client):
    return RecordHelper(client)

class TestGetRecordById:

    @allure.feature("Records")
    @allure.title("Get record by ID successfully")
    def test_get_record_by_id(self, record_helper):

        # --- Create input for get record by ID ---
        with allure.step("Build input for get record by ID"):
            input_data = build_get_record_by_id_input(
                record_id=TEST_RECORD_ID
            )

        # --- Execute get record by ID query ---
        with allure.step("Return record by ID"):
            response = record_helper.get_record_by_id(input_data)

        # --- Assertions for get record by ID response ---
        with allure.step("Validate response fields"):
            assert response["id"] and response["id"] != ""
            assert response["conversationId"] == TEST_RECORD_ID
            assert response["topic"] == TEST_RECORD_TOPIC_NAME
            assert response["duration"] and response["duration"] != ""