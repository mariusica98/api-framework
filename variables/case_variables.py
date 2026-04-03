from utils.test_data import *

 # CREATE CASE INPUTS
CREATE_CASE_INPUT = {
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

CREATE_CASE_EMPTY_STATUS_INPUT = {
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
            "caseStatus": "",
            "contentStatus": "NEW",
            "contentRiskRating": "Info",
            "caseThreadId": ""
        }
    }
}

CREATE_CASE_EMPTY_INITIAL_CASE_CONTENT_STATUS_INPUT = {
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
            "contentStatus": "",
            "contentRiskRating": "Info",
            "caseThreadId": ""
        }
    }
}   

# GET CASES INPUTS
GET_CASE_BY_ID_INPUT = {
    "id": None, 
    "auth": {
        "locale": "ro-RO",
        "timeZone": -120,
        "timeZoneId": "Europe/Bucharest"
    }
}

GET_ALL_CASES_INPUT = {
    "auth": {
        "locale": "ro-RO",
        "timeZone": -120,
        "timeZoneId": "Europe/Bucharest"
    },
    "filter": "AllItems"
}

# DELETE CASE INPUT
DELETE_CASE_BY_ID_INPUT_TEMPLATE = {
    "conversationSafeFolder": None  
}