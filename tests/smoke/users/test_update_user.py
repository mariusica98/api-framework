import pytest
import allure

from config.graphql_client import GraphQLClient
from utils.helper.user_helper import UserHelper
from utils.test_data import TEST_POLICY_RULE_ZQA_BULK_ID, TEST_USER_DEV_07_ID
from variables.user_variables import (
    build_update_user_input,
    DEFAULT_USER_UPDATE_PARAMS
)

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()

@pytest.fixture(scope="module")
def user_helper(client):
    return UserHelper(client)

class TestUpdateUserFlow:

    @allure.feature("User Management")
    @allure.title("Update user recording rules")
    def test_update_user_recording_rules(self, user_helper):


       # --- Input for update user Recording rules ---
        update_input = build_update_user_input(
            user_id=TEST_USER_DEV_07_ID,
            recording_rules=TEST_POLICY_RULE_ZQA_BULK_ID,
            **DEFAULT_USER_UPDATE_PARAMS
        )

        # --- Update user recording rules ---
        with allure.step("Update user recording rules"):
            response = user_helper.update_user(update_input)

        # --- Assertion for update user recording rules response ---
        with allure.step("Verify response"):
            assert response is not None
            assert response[0]["__typename"] == "UserData"