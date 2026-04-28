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

@pytest.fixture
def cleanup_context(case_helper, report_helper):
    context = {
        "case_id": None,
        "report": None
    }

    yield context

    with allure.step("Cleanup: deleting created entities"):
        if context["report"]:
            report_helper.delete_report_by_id(context["report"]["id"])
        if context["case_id"]:
            case_helper.delete_case_by_id(context["case_id"])

class TestCreateReportFlow:

    # --- Case Management KPI ---

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Case Compliance Rate KPI")
    def test_create_report_case_compliance_rate(self, case_helper, report_helper, cleanup_context):

        case_id = None
        report = None

        # --- Create case ---
        with allure.step("Creating case"):
            case_input = build_create_case_input(**DEFAULT_CASE_INPUT_PARAMS)
            case_folder = case_helper.create_case(case_input)
            case_id = case_folder["id"]
            cleanup_context["case_id"] = case_id

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
            cleanup_context["report"] = report

        # --- Assertion for created report ---
        with allure.step("Verifying created report"):
            report_id = report["id"]
            assert isinstance(report_id, str) and report_id != "", \
                f"Expected non-empty report_id, got {report_id!r}"

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Case Escalation Rate KPI")
    def test_create_report_case_escalation_rate(self, case_helper, report_helper, cleanup_context):

        case_id = None
        report = None

        # --- Create case ---
        with allure.step("Creating case"):
            case_input = build_create_case_input(**DEFAULT_CASE_INPUT_PARAMS)
            case_folder = case_helper.create_case(case_input)
            case_id = case_folder["id"]
            cleanup_context["case_id"] = case_id

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
            cleanup_context["report"] = report

        # --- Assertion for created report ---
        with allure.step("Verifying created report"):
            report_id = report["id"]
            assert isinstance(report_id, str) and report_id != "", \
                f"Expected non-empty report_id, got {report_id!r}"

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Case Resolution Time KPI")
    def test_create_report_case_resolution_time(self, case_helper, report_helper, cleanup_context):

        case_id = None
        report = None

        # --- Create case ---
        with allure.step("Creating case"):
            case_input = build_create_case_input(**DEFAULT_CASE_INPUT_PARAMS)
            case_folder = case_helper.create_case(case_input)
            case_id = case_folder["id"]
            cleanup_context["case_id"] = case_id

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
            cleanup_context["report"] = report

        # --- Assertion for created report ---
        with allure.step("Verifying created report"):
            report_id = report["id"]
            assert isinstance(report_id, str) and report_id != "", \
                f"Expected non-empty report_id, got {report_id!r}"

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Overall Compliance Rate KPI")
    def test_create_report_overall_compliance_rate(self, report_helper, cleanup_context):

        report = None

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
            cleanup_context["report"] = report

        # --- Assertion for created report ---
        with allure.step("Verifying created report"):
            report_id = report["id"]
            assert isinstance(report_id, str) and report_id != "", \
                f"Expected non-empty report_id, got {report_id!r}"

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Overall Escalation Rate KPI")
    def test_create_report_overall_escalation_rate(self, report_helper, cleanup_context):

        report = None

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
            cleanup_context["report"] = report

        # --- Assertion for created report ---
        with allure.step("Verifying created report"):
            report_id = report["id"]
            assert isinstance(report_id, str) and report_id != "", \
                f"Expected non-empty report_id, got {report_id!r}"

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Overall Resolution Time KPI")
    def test_create_report_overall_resolution_time(self, case_helper, report_helper, cleanup_context):

        case_id = None
        report = None

        # --- Create case ---
        with allure.step("Creating case"):
            case_input = build_create_case_input(**DEFAULT_CASE_INPUT_PARAMS)
            case_folder = case_helper.create_case(case_input)
            case_id = case_folder["id"]
            cleanup_context["case_id"] = case_id

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
            cleanup_context["report"] = report

        # --- Assertion for created report ---
        with allure.step("Verifying created report"):
            report_id = report["id"]
            assert isinstance(report_id, str) and report_id != "", \
                f"Expected non-empty report_id, got {report_id!r}"
    
    # --- Recording KPI ---

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Total Number KPI")
    def test_create_report_total_number(self, report_helper, cleanup_context):

        report = None

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
            cleanup_context["report"] = report

        # --- Assertion for created report ---
        with allure.step("Verifying created report"):
            report_id = report["id"]
            assert isinstance(report_id, str) and report_id != "", \
                f"Expected non-empty report_id, got {report_id!r}"

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Recorded Calls to Total KPI")
    def test_create_report_recorded_calls_to_total(self, report_helper, cleanup_context):

        report = None

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
            cleanup_context["report"] = report

        # --- Assertion for created report ---
        with allure.step("Verifying created report"):
            report_id = report["id"]
            assert isinstance(report_id, str) and report_id != "", \
                f"Expected non-empty report_id, got {report_id!r}"

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Pending Archive KPI")
    def test_create_report_pending_archive(self, report_helper, cleanup_context):

        report = None

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
            cleanup_context["report"] = report

        # --- Assertion for created report ---
        with allure.step("Verifying created report"):
            report_id = report["id"]
            assert isinstance(report_id, str) and report_id != "", \
                f"Expected non-empty report_id, got {report_id!r}"

    # --- Audit KPI ---

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Current Calls KPI")
    def test_create_report_current_calls(self, report_helper, cleanup_context):

        report = None

        # --- Prepare report input ---
        with allure.step("Preparing report input"):
            report_input = build_create_report_input(
                **{
                    **DEFAULT_REPORT_INPUT_PARAMS,
                    "kpi": TEST_REPORT_CURRENT_CALLS_KPI
                }
            )
            report_input["id"] = str(uuid.uuid4())

        # --- Create report ---
        with allure.step("Creating the report - Current Calls KPI"):
            report = report_helper.create_report(report_input)
            cleanup_context["report"] = report

        # --- Assertion for created report ---
        with allure.step("Verifying created report"):
            report_id = report["id"]
            assert isinstance(report_id, str) and report_id != "", \
                f"Expected non-empty report_id, got {report_id!r}"

    @allure.feature("Reports")
    @allure.title("Create Report successfully - Audit Logs KPI")
    def test_create_report_audit_logs(self, report_helper, cleanup_context):

        report = None

        # --- Prepare report input ---
        with allure.step("Preparing report input"):
            report_input = build_create_report_input(
                **{
                    **DEFAULT_REPORT_INPUT_PARAMS,
                    "kpi": TEST_REPORT_AUDIT_LOGS_KPI
                }
            )
            report_input["id"] = str(uuid.uuid4())

        # --- Create report ---
        with allure.step("Creating the report - Audit Logs KPI"):
            report = report_helper.create_report(report_input)
            cleanup_context["report"] = report
            
        # --- Assertion for created report ---
        with allure.step("Verifying created report"):
            report_id = report["id"]
            assert isinstance(report_id, str) and report_id != "", \
                f"Expected non-empty report_id, got {report_id!r}"