import pytest
import allure

from config.graphql_client import GraphQLClient
from utils.helper.user_helper import UserHelper
from utils.test_data import TEST_COMPLIANCE_VOICE_RECORDING_POLICY_LICENCE_ID, TEST_USER_06_DEV2_EMAIL, TEST_USER_06_DEV2_ID, TEST_USER_06_DEV2_NAME
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
    @allure.title("Add user - Compliance Voice Recording license")
    def test_add_user_compliance_voice_recording_licence(self, user_helper, cleanup_context):

        # --- Input data for add user ---
        input_data = build_create_user_input(
            user_id=TEST_USER_06_DEV2_ID,
            name=TEST_USER_06_DEV2_NAME,
            username=TEST_USER_06_DEV2_EMAIL,
            license=TEST_COMPLIANCE_VOICE_RECORDING_POLICY_LICENCE_ID
        )

        # --- Add user ---
        with allure.step("Add user with Compliance Voice Recording license"):
            response = user_helper.create_user(input_data)

        # --- Assertions for add user ---
        with allure.step("Verify response"):
            assert response is not None
            assert response["__typename"] == "UserData"
            assert response["name"] == TEST_USER_06_DEV2_NAME
        
        # --- Get id by user name ---
        user = user_helper.find_user_by_name(TEST_USER_06_DEV2_NAME)
        user_id = user["id"]

        # --- Store id for cleanup ---
        cleanup_context["user_id"] = user_id