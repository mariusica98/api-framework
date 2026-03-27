from utils.test_data import *

create_case_input = {
    "auth": {
        "locale": "en-US",
        "timeZone": -120,
        "timeZoneId": "Europe/Bucharest"
    },
    "conversationSafeFolder": {
        "id": "",
        "name": TEST_CASE_NAME,
        "description": TEST_CASE_DESCRIPTION,
        "supervisors": [],
        "conversations": [],
        "userId": "",
        "tenantId": "",
        "visibilityDetails": {
            "visibilityDetailsActive": False,
            "visibilityDetailsTranscript": False,
            "visibilityDetailsAnalytics": False,
            "visibilityDetailsAnalyticsChange": False,
            "visibilityDetailsMetadata": False,
            "visibilityDetailsTTL": False,
            "visibilityDetailsCustomFields": False,
            "visibilityDetailsNotes": False,
            "visibilityDetailsReplay": False,
            "visibilityDetailsQM": False,
            "visibilityCleanUp": False,
            "visibilityExport": False
        },
        "addConversations": False,
        "removeConversations": False,
        "exportFolders": False,
        "allowedInPolicy": False,
        "isCaseManagement": True,
        "caseManagementDetails": {
            "reviewers": [],
            "observers": [],
            "legalHold": False,
            "caseStatus": "OPEN",
            "contentStatus": "NEW",
            "contentRiskRating": "Info",
            "caseThreadId": ""
        }
    }
}


