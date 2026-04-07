import pytest
import allure
import uuid
from utils.report_helper import ReportHelper
from utils.case_helper import CaseHelper
from variables.case_variables import DEFAULT_CASE_INPUT_PARAMS, build_create_case_input
from variables.report_variables import DEFAULT_REPORT_INPUT_PARAMS, build_create_report_input
from utils.test_data import *
from config.graphql_client import GraphQLClient

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()

@pytest.fixture(scope="module")
def case_helper(client):
    return CaseHelper(client)

@pytest.fixture(scope="module")
def report_helper(client):
    return ReportHelper(client)

class TestCreateReportFlow:

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Case Compliance Rate KPI")
    def test_create_report_case_compliance_rate_successfully(self, case_helper, report_helper):

        case_id = None
        report = None

        try:
            # --- Create case ---
            with allure.step("Creating a case for report categories"):
                case_input = build_create_case_input(**DEFAULT_CASE_INPUT_PARAMS)
                case_folder = case_helper.create_case(case_input)
                case_id = case_folder["id"]

            assert isinstance(case_id, str) and case_id != "", \
                f"Expected non-empty case_id, got {case_id!r}"

            # --- Prepare report input ---
            with allure.step("Preparing report input linked to the case"):
                report_input = build_create_report_input(
                    **{
                        **DEFAULT_REPORT_INPUT_PARAMS,
                        "categories": case_id, 
                        "kpi": TEST_REPORT_CASE_COMPLIANCE_RATE_KPI
                    }
                )
                report_input["id"] = str(uuid.uuid4())

            # --- Create report ---
            with allure.step("Creating the report"):
                report = report_helper.create_report(report_input)

            # --- Assertion for created report ---
            with allure.step("Verifying created report"):
                report_id = report["id"]
                assert isinstance(report_id, str) and report_id != "", \
                    f"Expected non-empty report_id, got {report_id!r}"

        finally:
            # --- CLEANUP: Delete report and case---
            with allure.step("Deleting the case and report"):
                if report:
                    report_helper.delete_report_by_id(report["id"])
                if case_id:
                    case_helper.delete_case_by_id(case_id)
                print("ceva")
