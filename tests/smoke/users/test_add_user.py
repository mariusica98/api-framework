import pytest
import allure

from config.graphql_client import GraphQLClient
from utils.helper.user_helper import UserHelper
from utils.test_data import TEST_COMPLIANCE_VOICE_RECORDING_POLICY_ID, TEST_USER_06_DEV2_EMAIL, TEST_USER_06_DEV2_ID, TEST_USER_06_DEV2_NAME
from variables.user_variables import build_create_user_input

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()


@pytest.fixture(scope="module")
def user_helper(client):
    return UserHelper(client)

class TestCreateUserFlow:

    @allure.feature("User Management")
    @allure.title("Create user - Compliance Voice Recording license")
    def test_create_user_compliance_voice_recording(self, user_helper):

        input_data = build_create_user_input(
            user_id=TEST_USER_06_DEV2_ID,
            name=TEST_USER_06_DEV2_NAME,
            username=TEST_USER_06_DEV2_EMAIL,
            license=TEST_COMPLIANCE_VOICE_RECORDING_POLICY_ID
        )

        with allure.step("Create user with license 6"):
            response = user_helper.create_user(input_data)

        with allure.step("Verify response"):
            assert response is not None
            assert response["__typename"] == "UserData"
            assert response["name"] == TEST_USER_06_DEV2_NAME