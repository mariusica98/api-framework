import pytest
import allure

from config.graphql_client import GraphQLClient
from utils.helper.user_helper import UserHelper
from utils.test_data import *
from variables.user_variables import (
    build_create_user_input,
    build_delete_user_input,
    build_update_user_input,
)

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()

@pytest.fixture(scope="module")
def user_helper(client):
    return UserHelper(client)

@pytest.fixture
def cleanup_context(user_helper):
    context = {
        "user_id": None
    }

    yield context

    if context["user_id"]:
        with allure.step("Cleanup: deleting created user"):
            delete_input = build_delete_user_input(
                user_id=context["user_id"]
            )
            user_helper.delete_user(delete_input)

class TestUpdateUserFlow:

    @allure.feature("User Management")
    @allure.title("Update user")
    def test_update_user(self, user_helper, cleanup_context):

        # --- CREATE user with Recording policy licence ---
        with allure.step("Create user"):
            create_input = build_create_user_input(
                user_id=TEST_USER_06_DEV2_ID,
                name=TEST_USER_06_DEV2_NAME,
                username=TEST_USER_06_DEV2_EMAIL,
                license=TEST_COMPLIANCE_VOICE_RECORDING_POLICY_LICENE_ID
            )

            create_response = user_helper.create_user(create_input)

        # ---------- GET CREATED USER ----------
        with allure.step("Get created user ID"):
            user = user_helper.find_user_by_name(TEST_USER_06_DEV2_NAME)
            assert user is not None

            user_id = user["id"]
            cleanup_context["user_id"] = user_id

        # ---------- Input for update user ----------
        with allure.step("Create user update input"):
            update_input = build_update_user_input(
                user_id=user_id,
                # Rules
                recording_rules=TEST_RECORDING_RULE_ZQA_BULK_ID,
                replay=TEST_REPLAY_RULE_EQA_REPLAY_ALL_ID,
                access=TEST_ACCESS_RULE_ADMINISTRATOR_ID,
                analytics=TEST_ANALYTICS_RULE_ANALYZE_ALL_ID,
                storageId=TEST_STORAGE_RULE_ID,
                # ADD-ONS
                addOnAnalytics=True,
                addOnCaseManagement=True,
                addOnEmail=True,
            )

        # ---------- Update user ----------
        with allure.step("Update user"):
            update_response = user_helper.update_user(update_input)

        # ---------- ASSERT ----------
        with allure.step("Verify update response"):
            assert update_response is not None
            assert update_response[0]["__typename"] == "UserData"