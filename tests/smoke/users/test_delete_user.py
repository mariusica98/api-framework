import allure
import pytest

from config.graphql_client import GraphQLClient
from utils.helper.user_helper import UserHelper
from variables.user_variables import build_create_user_input, build_delete_user_input
from utils.test_data import *

@pytest.fixture(scope="module")
def user_helper(client):
    return UserHelper(client)

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()

class TestDeleteUserFlow:

    @allure.feature("User Management")
    @allure.title("Delete user and verify removal")
    def test_delete_user(self, user_helper):

        # --- Input for create user ---
        with allure.step("Input for create user"):
            input_data = build_create_user_input(
                user_id=TEST_USER_06_DEV2_ID,
                name=TEST_USER_06_DEV2_NAME,
                username=TEST_USER_06_DEV2_EMAIL,
                license=TEST_COMPLIANCE_VOICE_RECORDING_POLICY_LICENE_ID
            )
        
        # --- Create user ---
        with allure.step(f"Create user"):
            user_helper.create_user(input_data)

        # --- Get user ID ---
        with allure.step("Get user ID"):
            user = user_helper.find_user_by_name(TEST_USER_06_DEV2_NAME)
            user_id = user.get("id") or user.get("user_id") or user.get("userId")

        # --- Delete user---
        with allure.step("Delete the created user"):
            delete_input = build_delete_user_input(user_id=user_id)
            user_helper.delete_user(delete_input)

        # --- Get user by id to check user deletion ---
        with allure.step("Get user by ID to check the deletion"):
            deleted_user = user_helper.find_user_by_name(TEST_USER_06_DEV2_NAME)
        
        # --- Assertion for delete user
        with allure.step("Check the user deletion"):
            assert deleted_user is None