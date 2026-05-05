import pytest
import allure
from config.graphql_client import *
from utils.helper.record_helper import *
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
    
    @allure.feature("Records")
    @allure.title("Get record by ID with error - invalid record ID")
    def test_get_record_by_invalid_id(self, record_helper):

        # --- Input for invalid record ID ---
        with allure.step("Build input for invalid record ID"):
            input_data = build_get_record_by_id_input(
                record_id=TEST_RECORD_INVALID_ID
            )

        # --- Execute query ---
        with allure.step("Execute get record by invalid ID query"):
            response = record_helper.get_record_by_id(input_data)

        # --- Assertion for get record by invalid ID ---
        with allure.step("Validate response for invalid record ID is None"):
            assert response is None

    @allure.feature("Records")
    @allure.title("Get all records successfully")
    def test_get_all_records(self, record_helper):

        # --- Input for get all records ---
        with allure.step("Create input for get all records"):
            input_data = build_get_all_records_input()

        # --- Execute get all records query ---
        with allure.step("Execute get all records query"):
            response = record_helper.get_all_records(input_data)

        # --- Assertions for get all records list---
        with allure.step("Validate get all records response list"):
            assert "days" in response
            assert isinstance(response["days"], list)
            assert len(response["days"]) > 0
        
        # --- Assertions for first record in the list ---
        with allure.step("Validate first day content exists"):
            first_day = response["days"][0]
            assert "content" in first_day
            assert isinstance(first_day["content"], list)
            assert len(first_day["content"]) > 0
        
        # --- Assertions for first record structure ---
        with allure.step("Validate first record structure"):
            first_record = first_day["content"][0]
            assert first_record["id"]
            assert first_record["conversationId"]
            assert first_record["topic"]
            assert first_record["duration"]
            assert first_record["id"] != ""
            assert first_record["conversationId"] != ""
            assert first_record["topic"] != ""
            assert first_record["duration"] != ""