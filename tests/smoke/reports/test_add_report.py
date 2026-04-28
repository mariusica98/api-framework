import pytest
import allure
import uuid
from utils.helper.report_helper import ReportHelper
from utils.helper.conversation_safe_folder_helper.case_helper import CaseHelper
from variables.conversation_safe_variables.case_variables import DEFAULT_CASE_INPUT_PARAMS, build_create_case_input
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

    # --- Case Management KPI ---

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Case Compliance Rate KPI")
    def test_create_report_case_compliance_rate(self, case_helper, report_helper):

        case_id = None
        report = None

        try:
            # --- Create case ---
            with allure.step("Creating case"):
                case_input = build_create_case_input(**DEFAULT_CASE_INPUT_PARAMS)
                case_folder = case_helper.create_case(case_input)
                case_id = case_folder["id"]

            assert isinstance(case_id, str) and case_id != "", \
                f"Expected non-empty case_id, got {case_id!r}"

            # --- Prepare report input ---
            with allure.step("Preparing report input"):
                report_input = build_create_report_input(
                    **{
                        **DEFAULT_REPORT_INPUT_PARAMS,
                        "categories": case_id, 
                        "kpi": TEST_REPORT_CASE_COMPLIANCE_RATE_KPI
                    }
                )
                report_input["id"] = str(uuid.uuid4())

            # --- Create report ---
            with allure.step("Creating the report - Case Compliance Rate KPI"):
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

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Case Escalation Rate KPI")
    def test_create_report_case_escalation_rate(self, case_helper, report_helper):

        case_id = None
        report = None

        try:
            # --- Create case ---
            with allure.step("Creating case"):
                case_input = build_create_case_input(**DEFAULT_CASE_INPUT_PARAMS)
                case_folder = case_helper.create_case(case_input)
                case_id = case_folder["id"]

            assert isinstance(case_id, str) and case_id != "", \
                f"Expected non-empty case_id, got {case_id!r}"

            # --- Prepare report input ---
            with allure.step("Preparing report input"):
                report_input = build_create_report_input(
                    **{
                        **DEFAULT_REPORT_INPUT_PARAMS,
                        "categories": case_id, 
                        "kpi": TEST_REPORT_CASE_ESCALATION_RATE_KPI
                    }
                )
                report_input["id"] = str(uuid.uuid4())

            # --- Create report ---
            with allure.step("Creating the report - Case Escalation Rate KPI"):
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

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Case Resolution Time KPI")
    def test_create_report_case_resolution_time(self, case_helper, report_helper):

        case_id = None
        report = None

        try:
            # --- Create case ---
            with allure.step("Creating case"):
                case_input = build_create_case_input(**DEFAULT_CASE_INPUT_PARAMS)
                case_folder = case_helper.create_case(case_input)
                case_id = case_folder["id"]

            assert isinstance(case_id, str) and case_id != "", \
                f"Expected non-empty case_id, got {case_id!r}"

            # --- Prepare report input ---
            with allure.step("Preparing report input"):
                report_input = build_create_report_input(
                    **{
                        **DEFAULT_REPORT_INPUT_PARAMS,
                        "categories": case_id, 
                        "kpi": TEST_REPORT_CASE_RESOLUTION_TIME_KPI
                    }
                )
                report_input["id"] = str(uuid.uuid4())

            # --- Create report ---
            with allure.step("Creating the report - Case Resolution Time KPI"):
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

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Overall Compliance Rate KPI")
    def test_create_report_overall_compliance_rate(self, report_helper):

        report = None

        try:
            # --- Prepare report input ---
            with allure.step("Preparing report input"):
                report_input = build_create_report_input(
                    **{
                        **DEFAULT_REPORT_INPUT_PARAMS,
                        "kpi": TEST_REPORT_OVERALL_COMPLIANCE_RATE_KPI
                    }
                )
                report_input["id"] = str(uuid.uuid4())

            # --- Create report ---
            with allure.step("Creating the report - Overall Compliance Rate KPI"):
                report = report_helper.create_report(report_input)

            # --- Assertion for created report ---
            with allure.step("Verifying created report"):
                report_id = report["id"]
                assert isinstance(report_id, str) and report_id != "", \
                    f"Expected non-empty report_id, got {report_id!r}"

        finally:
            # --- CLEANUP: Delete report ---
            with allure.step("Deleting the report"):
                if report:
                    report_helper.delete_report_by_id(report["id"])

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Overall Escalation Rate KPI")
    def test_create_report_overall_escalation_rate(self, report_helper):

        report = None

        try:
            # --- Prepare report input ---
            with allure.step("Preparing report input"):
                report_input = build_create_report_input(
                    **{
                        **DEFAULT_REPORT_INPUT_PARAMS,
                        "kpi": TEST_REPORT_OVERALL_ESCALATION_RATE_KPI
                    }
                )
                report_input["id"] = str(uuid.uuid4())

            # --- Create report ---
            with allure.step("Creating the report - Overall Escalation Rate KPI"):
                report = report_helper.create_report(report_input)

            # --- Assertion for created report ---
            with allure.step("Verifying created report"):
                report_id = report["id"]
                assert isinstance(report_id, str) and report_id != "", \
                    f"Expected non-empty report_id, got {report_id!r}"

        finally:
            # --- CLEANUP: Delete report ---
            with allure.step("Deleting the report"):
                if report:
                    report_helper.delete_report_by_id(report["id"])
    
    @allure.feature("Reports")
    @allure.title("Create Report successfully - Overall Resolution Time KPI")
    def test_create_report_overall_resolution_time(self, case_helper, report_helper):

        case_id = None
        report = None

        try:
            # --- Create case ---
            with allure.step("Creating case"):
                case_input = build_create_case_input(**DEFAULT_CASE_INPUT_PARAMS)
                case_folder = case_helper.create_case(case_input)
                case_id = case_folder["id"]

            assert isinstance(case_id, str) and case_id != "", \
                f"Expected non-empty case_id, got {case_id!r}"

            # --- Prepare report input ---
            with allure.step("Preparing report input"):
                report_input = build_create_report_input(
                    **{
                        **DEFAULT_REPORT_INPUT_PARAMS,
                        "categories": case_id, 
                        "kpi": TEST_REPORT_OVERALL_RESOLUTION_TIME_KPI
                    }
                )
                report_input["id"] = str(uuid.uuid4())

            # --- Create report ---
            with allure.step("Creating the report - Overall Resolution Time KPI"):
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
    
    # --- Recording KPI ---

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Total Number KPI")
    def test_create_report_total_number(self, report_helper):

        report = None

        try:
            # --- Prepare report input ---
            with allure.step("Preparing report input"):
                report_input = build_create_report_input(
                    **{
                        **DEFAULT_REPORT_INPUT_PARAMS,
                        "kpi": TEST_REPORT_TOTAL_NUMBER_KPI
                    }
                )
                report_input["id"] = str(uuid.uuid4())

            # --- Create report ---
            with allure.step("Creating the report - Total Number KPI"):
                report = report_helper.create_report(report_input)

            # --- Assertion for created report ---
            with allure.step("Verifying created report"):
                report_id = report["id"]
                assert isinstance(report_id, str) and report_id != "", \
                    f"Expected non-empty report_id, got {report_id!r}"

        finally:
            # --- CLEANUP: Delete report ---
            with allure.step("Deleting the report"):
                if report:
                    report_helper.delete_report_by_id(report["id"])

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Recorded Calls to Total KPI")
    def test_create_report_recorded_calls_to_total(self, report_helper):

        report = None

        try:
            # --- Prepare report input ---
            with allure.step("Preparing report input"):
                report_input = build_create_report_input(
                    **{
                        **DEFAULT_REPORT_INPUT_PARAMS,
                        "kpi": TEST_REPORT_RECORDED_CALLS_TO_TOTAL_KPI
                    }
                )
                report_input["id"] = str(uuid.uuid4())

            # --- Create report ---
            with allure.step("Creating the report - Recorded Calls to Total KPI"):
                report = report_helper.create_report(report_input)

            # --- Assertion for created report ---
            with allure.step("Verifying created report"):
                report_id = report["id"]
                assert isinstance(report_id, str) and report_id != "", \
                    f"Expected non-empty report_id, got {report_id!r}"

        finally:
            # --- CLEANUP: Delete report ---
            with allure.step("Deleting the report"):
                if report:
                    report_helper.delete_report_by_id(report["id"])

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Pending Archive KPI")
    def test_create_report_pending_archive(self, report_helper):

        report = None

        try:
            # --- Prepare report input ---
            with allure.step("Preparing report input"):
                report_input = build_create_report_input(
                    **{
                        **DEFAULT_REPORT_INPUT_PARAMS,
                        "kpi": TEST_REPORT_PENDING_ARCHIVE_KPI
                    }
                )
                report_input["id"] = str(uuid.uuid4())

            # --- Create report ---
            with allure.step("Creating the report - Pending Archive KPI"):
                report = report_helper.create_report(report_input)

            # --- Assertion for created report ---
            with allure.step("Verifying created report"):
                report_id = report["id"]
                assert isinstance(report_id, str) and report_id != "", \
                    f"Expected non-empty report_id, got {report_id!r}"

        finally:
            # --- CLEANUP: Delete report ---
            with allure.step("Deleting the report"):
                if report:
                    report_helper.delete_report_by_id(report["id"])
