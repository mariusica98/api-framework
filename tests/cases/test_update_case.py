import pytest
import allure
from config.graphql_client import GraphQLClient
from models.case_error import *
from utils.case_helper import CaseHelper
from variables.case_variables import *

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()

@pytest.fixture(scope="module")
def case_helper(client):
    return CaseHelper(client)

class TestUpdateCaseFlow:

    @allure.feature("Case Management")
    @allure.title("Get Case by ID successfully with full verification")
    def test_get_case_by_id(self, case_helper):

        case_folder = None
        case_id = None
        try:
            # --- Create case ---
            with allure.step("Creating a case to be updated"):
                case_folder = case_helper.create_case(CREATE_CASE_INPUT)
                case_id = case_folder["id"]

            # --- Prepare data for Update case ---
            update_data = UPDATE_CASE_INPUT.copy()
            update_data["conversationSafeFolder"]["id"] = case_id
            update_data["conversationSafeFolder"]["name"] = TEST_CASE_UPDATED_NAME
            update_data["conversationSafeFolder"]["description"] = TEST_CASE_DESCRIPTION_UPDATED
            update_data["conversationSafeFolder"]["userId"] = TEST_USER_ID
            update_data["conversationSafeFolder"]["tenantId"] = TEST_TENANT_ID

            # ---- Update case ---
            with allure.step("Updating the case"):
                case_helper.update_case(case_id, update_data)

            # --- Get case by ID for verification ---
            with allure.step("Getting case by ID"):
                case_data = case_helper.get_case_by_id(case_id)

            # --- Assertions for full verification ---
            with allure.step("Verifying case data"):
                # General info
                assert case_data["id"] == case_id
                assert case_data["name"] == TEST_CASE_UPDATED_NAME
                assert case_data["description"] == TEST_CASE_DESCRIPTION_UPDATED

                cmd = case_data["caseManagementDetails"]
                assert cmd["caseStatus"] == TEST_CASE_STATUS_IN_PROGRESS, \
                    f"Expected caseStatus {TEST_CASE_STATUS_IN_PROGRESS}, got {cmd['caseStatus']!r}"
                assert cmd["contentStatus"] == TEST_CASE_CONTENT_STATUS_ESCALED, \
                    f"Expected contentStatus {TEST_CASE_CONTENT_STATUS_ESCALED}, got {cmd['contentStatus']!r}"
                assert cmd["contentRiskRating"] == TEST_CASE_RISK_RATING_ADHERANCE, \
                    f"Expected contentRiskRating {TEST_CASE_RISK_RATING_ADHERANCE}, got {cmd['contentRiskRating']!r}"

        finally:
            with allure.step("Deleting the case"):
                if case_id:
                    case_helper.delete_case_by_id(case_id)