import pytest
from config.graphql_client import GraphQLClient
from utils.case_helper import CaseHelper
from variables.case_variables import CREATE_CASE_INPUT
import allure

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()

@pytest.fixture(scope="module")
def case_helper(client):
    return CaseHelper(client)

class TestGetCaseFlow:

    @allure.feature("Case Management")
    @allure.title("Get Case by ID successfully")
    def test_get_case_by_id(self, case_helper):

        case_id = None
        try:
             # --- Create case  ---
            with allure.step("Creating a new case for GET"):
                case_folder = case_helper.create_case(CREATE_CASE_INPUT)
                case_id = case_folder["id"]

            # --- Get case  ---
            with allure.step("Getting case by ID"):
                case_data = case_helper.get_case_by_id(case_id)

             # --- Assertions for get ---
            with allure.step("Verifying case data"):
                assert case_data["id"] == case_id
                assert case_data["name"] == CREATE_CASE_INPUT["conversationSafeFolder"]["name"]
                assert case_data["description"] == CREATE_CASE_INPUT["conversationSafeFolder"]["description"]
                assert case_data["isCaseManagement"] is True

        finally:
            with allure.step("Deleting the case"):
                if case_id:
                    case_helper.delete_case_by_id(case_id)