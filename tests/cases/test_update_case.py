import pytest
import allure
from config.graphql_client import GraphQLClient
from models.case_error import *
from utils.case_helper import CaseHelper
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
            # --- Create case ---
            with allure.step("Creating a case to be updated"):
                case_folder = case_helper.create_case(CREATE_CASE_INPUT_1)
                case_id = case_folder["id"]

            # ---- Update case ---
            with allure.step("Updating the case"):
                case_helper.update_case(case_id, UPDATE_CASE_INPUT)
            
            # --- Assertions for update case ---
            with allure.step("Verifying updated case response"):
                assert isinstance(case_id, str) and case_id != "", \
                    f"Expected non-empty string for id, got: {case_id!r}"
                assert case_folder["status"] == "ok", \
                    f"Expected status 'ok', got: {case_folder['status']!r}"
                assert case_folder["text"] == "", \
                    f"Expected text to be empty string, got: {case_folder['text']!r}"

            # --- Get case by ID for full verification ---
            with allure.step("Getting case by ID (for full verification)"):
                case_data = case_helper.get_case_by_id(case_id)

            # --- Assertions for full verification (because the response from the update does not contain all the necessary data) ---
            with allure.step("Verify all the updated case data"):
                assert case_data["id"] == case_id
                assert case_data["name"] == TEST_CASE_NAME_UPDATED
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
    
    @allure.feature("Case Management")
    @allure.title("Update Case with error - duplicate name")
    def test_update_case_with_duplicate_name(self, case_helper):

        case_folder = case_folder_2 = None
        case_id = case_id_2 = None
        try:
            # --- Create first case ---
            with allure.step("Creating first case"):
                case_folder = case_helper.create_case(CREATE_CASE_INPUT_1)
                case_id = case_folder["id"]

            # --- Create second case  ---
            with allure.step("Creating the second case"):
                case_folder_2 = case_helper.create_case(CREATE_CASE_INPUT_2)
                case_id_2 = case_folder_2["id"]

            # --- Update with duplicate name ---
            with allure.step("Updating the second case with the first case's name"):
                response = case_helper.update_case(case_id_2, CREATE_CASE_INPUT_1)

            # --- Assertions for update with duplicate name error ---
            with allure.step("Verifying the response for duplicate name error"):
                assert response["status"] == "error", "Expected error status"
                assert response["text"] == "nameDuplicatedError", "Expected nameDuplicatedError text"

        finally:
            # --- Cleanup ---
            if case_id or case_id_2:
                with allure.step("Deleting the cases"):
                    if case_id:
                        case_helper.delete_case_by_id(case_id)
                    if case_id_2:
                        case_helper.delete_case_by_id(case_id_2)