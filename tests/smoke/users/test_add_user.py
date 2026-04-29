import pytest
import allure

from config.graphql_client import GraphQLClient
from utils.helper.user_helper import UserHelper
from utils.test_data import *
from variables.user_variables import build_create_user_input, build_delete_user_input

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

class TestCreateUserFlow:

    @allure.feature("User Management")
    @allure.title("Add user - All licences")
    @pytest.mark.parametrize(
        "license_id, description",
        [
            (TEST_COMPLIANCE_VOICE_RECORDING_POLICY_LICENCE_ID, "Compliance Voice Recording"),
            (TEST_COMPLIANCE_UC_RECORDING_LICENCE_ID, "Compliance UC Recording"),
            (TEST_SMART_VOICE_RECORDING_POLICY_ID, "Smart Voice Recording"),
            (TEST_SMART_UC_RECORDING_POLICY_ID, "Smart UC Recording"),
            (TEST_ENTRY_VOICE_RECORDING_POLICY_ID, "Entry Voice Recording"),
            (TEST_SMART_BASE_LICENCE_ID, "Smart Base Licence"),
            (TEST_COMPLIANCE_BASE_LICENCE_ID, "Compliance Base Licence"),
            (TEST_CHAT_RECORDING_STANDALONE_LICENCE_ID, "Chat Recording Standalone Licence"),
            (TEST_RECORDING_INSIGHTS_AI_LICENCE_ID, "Recording Insights AI Licence"),
            (TEST_COMPLIANCE_VOICE_RECORDING_AND_ANALYTICS_LICENCE_ID, "Compliance Voice Recording and Analytics Licence"),
            (TEST_COMPLIANCE_UC_RECORDING_AND_ANALYTICS_LICENCE_ID, "Compliance UC Recording and Analytics Licence"),
            (TEST_SMART_VOICE_AND_ANALYTICS_LICENCE_ID, "Smart Voice and Analytics Licence"),
            (TEST_SMART_UC_RECORDING_AND_ANALYTICS_LICENCE_ID, "Smart UC Recording and Analytics Licence"),
            
        ]
    )
    def test_add_user_with_various_licences(self, user_helper, cleanup_context, license_id, description):

        with allure.step(f"Input for {description}"):
            input_data = build_create_user_input(
                user_id=TEST_USER_06_DEV2_ID,
                name=TEST_USER_06_DEV2_NAME,
                username=TEST_USER_06_DEV2_EMAIL,
                license=license_id
            )

        with allure.step(f"Add user with {description} license"):
            response = user_helper.create_user(input_data)

        with allure.step("Verify response"):
            assert response is not None
            assert response["__typename"] == "UserData"
            assert response["name"] == TEST_USER_06_DEV2_NAME

        with allure.step("Get user ID for cleanup"):
            user = user_helper.find_user_by_name(TEST_USER_06_DEV2_NAME)
            cleanup_context["user_id"] = user["id"]