from utils.test_data import *

# Functions to build input data for reports operations
def build_create_report_input(
    *,
    report_id,
    title,
    kpi,
    categories,
    dashboard_id
):
    return {
        "id": report_id,
        "title": title,
        "kpi": kpi,
        "keyword": "",
        "sortOrder": 0,
        "widget": "Speedometer",
        "cycle": "ThisYear",
        "startDate": None,
        "endDate": None,
        "person": [],
        "type": "text",
        "valueType": "average",
        "tForm": "cycle",
        "alarming": None,
        "categories": categories,
        "reportSend": False,
        "jobType": {
            "intervalType": "Periodical",
            "intervalMonth": 0,
            "intervalDay": 0,
            "intervalHour": 0,
            "jobStartTime": None
        },
        "reportMail": "",
        "botAppId": None,
        "jobId": "",
        "dashboard": dashboard_id,
        "conversationType": [],
        "emailAttachmentFormat": "CSV_WITH_SEMICOLON",
        "problemTypes": [],
        "pstnNumber": "",
        "dtmfStartDate": None,
        "dtmfEndDate": None
    }

def build_delete_report_by_id_input(*, report_id):
    return {
        "input": {
            "locale": "ro-RO",
            "timeZone": -120,
            "timeZoneId": "Europe/Bucharest"
        },
        "id": report_id
    }

#  Default parameters for creating a report input
DEFAULT_REPORT_INPUT_PARAMS = {
    "report_id": TEST_REPORT_ID,
    "title": TEST_REPORT_TITLE,
    "kpi": "",
    "categories": "",
    "dashboard_id": TEST_API_DASHBOARD_ID
}
