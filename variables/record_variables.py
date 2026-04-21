from utils.test_data import *

# Functions to build input payloads for Record operations
def build_add_record_case_input(*, name, description, case_status, content_status, content_risk_rating, conversations=None, user_id="", tenant_id="", case_id=""):
    if conversations is None:
        conversations = []

    return {
        "auth": {
            "locale": "en-US",
            "timeZone": -120,
            "timeZoneId": "Europe/Bucharest"
        },
        "conversationSafeFolder": {
            "id": case_id,  
            "name": name,
            "description": description,
            "supervisors": [],
            "conversations": conversations,
            "userId": user_id,
            "tenantId": tenant_id,
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
            "addConversations": True,
            "removeConversations": False,
            "exportFolders": False,
            "allowedInPolicy": False,
            "isCaseManagement": True,
            "caseManagementDetails": {
                "reviewers": [],
                "observers": [],
                "legalHold": False,
                "caseStatus": case_status,
                "contentStatus": content_status,
                "contentRiskRating": content_risk_rating,
                "caseThreadId": ""
            }
        }
    }

def build_remove_record_case_input(*, conversation_ids, case_id):
    return {
        "auth": {
            "locale": "en-US",
            "timeZone": -120,
            "timeZoneId": "Europe/Bucharest"
        },
        "conversationId": conversation_ids,
        "selectedFolders": [case_id],
        "action": "remove",
        "riskRating": None
    }

# Default parameters for add record to case input
DEFAULT_ADD_RECORD_CASE_PARAMS = {
    "name": TEST_CASE_NAME_1,
    "description": TEST_CASE_DESCRIPTION,
    "case_status": TEST_CASE_STATUS_OPEN,
    "content_status": TEST_CASE_CONTENT_STATUS_NEW,
    "content_risk_rating": TEST_CASE_RISK_RATING_INFORMATION,
    "conversations": [],  
    "user_id": "",
    "tenant_id": "",
    "case_id": ""
}