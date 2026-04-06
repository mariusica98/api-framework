def build_create_case_input(*, name, description, case_status, content_status, content_risk_rating, user_id, tenant_id):
    return {
        "auth": {
            "locale": "en-US",
            "timeZone": -120,
            "timeZoneId": "Europe/Bucharest"
        },
        "conversationSafeFolder": {
            "id": "",
            "name": name,
            "description": description,
            "supervisors": [],
            "conversations": [],
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
            "addConversations": False,
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

def build_delete_case_input(*, case_id):
    return {
        "conversationSafeFolder": case_id
    }

def build_get_case_by_id_input(*, case_id):
    return {
        "id": case_id,
        "auth": {
            "locale": "ro-RO",
            "timeZone": -120,
            "timeZoneId": "Europe/Bucharest"
        }
    }

def build_get_all_cases_input(*, filter="AllItems"):
    return {
        "auth": {
            "locale": "ro-RO",
            "timeZone": -120,
            "timeZoneId": "Europe/Bucharest"
        },
        "filter": filter
    }

def build_update_case_input(*, name, description, case_status, content_status, content_risk_rating, user_id="", tenant_id=""):
    return {
        "auth": {
            "locale": "en-US",
            "timeZone": -120,
            "timeZoneId": "Europe/Bucharest"
        },
        "conversationSafeFolder": {
            "id": "",  
            "name": name,
            "description": description,
            "supervisors": [],
            "conversations": [],
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
            "addConversations": False,
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