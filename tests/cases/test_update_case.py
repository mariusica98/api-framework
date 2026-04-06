import pytest
import allure
from config.graphql_client import *
from models.case_error import *
from utils.case_helper import *
from variables.case_variables import *
from utils.test_data import *

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()

@pytest.fixture(scope="module")
def case_helper(client):
    return CaseHelper(client)

class TestUpdateCaseFlow:

    @allure.feature("Case Management")
    @allure.title("Update Case successfully")
    def test_update_case(self, case_helper):

        case_folder = None
        case_id = None
        try:
            #--- Input data for creating a case to be updated ---
            create_input = build_create_case_input(
                name=TEST_CASE_NAME_1,
                description=TEST_CASE_DESCRIPTION,
                case_status=TEST_CASE_STATUS_OPEN,
                content_status=TEST_CASE_CONTENT_STATUS_NEW,
                content_risk_rating=TEST_CASE_RISK_RATING_INFORMATION,
                user_id="",
                tenant_id=""
            )

            #--- Create a case to be updated ---
            with allure.step("Creating a case to be updated"):
                case_folder = case_helper.create_case(create_input)
                case_id = case_folder["id"]

            # --- Update case ---
            with allure.step("Updating the case"):
                update_input = build_update_case_input(
                    name=TEST_CASE_NAME_UPDATED,
                    description=TEST_CASE_DESCRIPTION_UPDATED,
                    case_status=TEST_CASE_STATUS_IN_PROGRESS,
                    content_status=TEST_CASE_CONTENT_STATUS_ESCALED,
                    content_risk_rating=TEST_CASE_RISK_RATING_ADHERANCE,
                    user_id=TEST_USER_ID,
                    tenant_id=TEST_TENANT_ID
                )
                case_helper.update_case(case_id, update_input)

            # --- Get case by ID for verification ---
            with allure.step("Getting case by ID for verification"):
                case_data = case_helper.get_case_by_id(case_id)

            # --- Assertions for updated case ---
            with allure.step("Verify updated case data"):
                assert case_data["id"] == case_id
                assert case_data["name"] == TEST_CASE_NAME_UPDATED
                assert case_data["description"] == TEST_CASE_DESCRIPTION_UPDATED

                cmd = case_data["caseManagementDetails"]
                assert cmd["caseStatus"] == TEST_CASE_STATUS_IN_PROGRESS
                assert cmd["contentStatus"] == TEST_CASE_CONTENT_STATUS_ESCALED
                assert cmd["contentRiskRating"] == TEST_CASE_RISK_RATING_ADHERANCE

        finally:
            # --- Cleanup ---
            with allure.step("Deleting the case"):
                if case_id:
                    case_helper.delete_case_by_id(case_id)
        
    @allure.feature("Case Management")
    @allure.title("Update Case with error - duplicate name")
    def test_update_case_with_duplicate_name(self, case_helper):

        case_folder_1 = case_folder_2 = None
        case_id_1 = case_id_2 = None
        try:
            # --- Input data for creating first case ---
            create_input_1 = build_create_case_input(
                name=TEST_CASE_NAME_1,
                description=TEST_CASE_DESCRIPTION,
                case_status=TEST_CASE_STATUS_OPEN,
                content_status=TEST_CASE_CONTENT_STATUS_NEW,
                content_risk_rating=TEST_CASE_RISK_RATING_INFORMATION,
                user_id="",
                tenant_id=""
            )

            #--- Create first case ---
            with allure.step("Creating first case"):
                case_folder_1 = case_helper.create_case(create_input_1)
                case_id_1 = case_folder_1["id"]

            # --- Input data for creating second case ---
            create_input_2 = build_create_case_input(
                name=TEST_CASE_NAME_2,
                description=TEST_CASE_DESCRIPTION,
                case_status=TEST_CASE_STATUS_OPEN,
                content_status=TEST_CASE_CONTENT_STATUS_NEW,
                content_risk_rating=TEST_CASE_RISK_RATING_INFORMATION,
                user_id="",
                tenant_id=""
            )
            
            #--- Create second case ---
            with allure.step("Creating the second case"):
                case_folder_2 = case_helper.create_case(create_input_2)
                case_id_2 = case_folder_2["id"]

            # --- Attempt to update second case with duplicate name ---
            with allure.step("Updating the second case with the first case's name"):
                update_input = build_update_case_input(
                    name=TEST_CASE_NAME_1, 
                    description=TEST_CASE_DESCRIPTION,
                    case_status=TEST_CASE_STATUS_OPEN,
                    content_status=TEST_CASE_CONTENT_STATUS_NEW,
                    content_risk_rating=TEST_CASE_RISK_RATING_INFORMATION,
                    user_id="",
                    tenant_id=""
                )
                response = case_helper.update_case(case_id_2, update_input)

            # --- Assertions for duplicate name error ---
            with allure.step("Verifying the response for duplicate name error"):
                assert response["status"] == "error", f"Expected error status, got: {response['status']!r}"
                assert response["text"] == "nameDuplicatedError", f"Expected text 'nameDuplicatedError', got: {response['text']!r}"

        finally:
            # --- Cleanup ---
            with allure.step("Deleting the cases"):
                if case_id_1:
                    case_helper.delete_case_by_id(case_id_1)
                if case_id_2:
                    case_helper.delete_case_by_id(case_id_2)