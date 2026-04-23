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

def build_bulk_export_input(
    *,
    list_id,
    zip_password,
    bulk_name,
    only_transcript,
    only_metadata,
    include_mail_body,
    include_mail_attachments
):
    return {
        "auth": {
            "locale": "ro-RO",
            "timeZone": -180,
            "timeZoneId": "Europe/Bucharest"
        },
        "listId": list_id,
        "zipPassword": zip_password,
        "bulkName": bulk_name,
        "onlyTranscript": only_transcript,
        "onlyMetadata": only_metadata,
        "includeMailBody": include_mail_body,
        "includeMailAttachemnts": include_mail_attachments
    }

def build_get_record_by_id_input(*, record_id, call_start_ms=None, is_history_vault=False):
    return {
        "id": record_id,
        "auth": {
            "locale": "ro-RO",
            "timeZone": -180,
            "timeZoneId": "Europe/Bucharest"
        },
        "callStartMs": call_start_ms,
        "isHistoryVault": is_history_vault
    }

def build_get_all_records_input(
    *,
    val="",
    filter=None,
    with_save=False,
    path=TEST_DEFAULT_RECORDS_PATH,
    search_in=None
):
    if search_in is None:
        search_in = []

    return {
        "val": val,
        "filter": filter,
        "withSave": with_save,
        "auth": {
            "locale": "ro-RO",
            "timeZone": -180,
            "timeZoneId": "Europe/Bucharest"
        },
        "path": path,
        "searchIn": search_in
    }

def build_add_record_to_folder_input(
    *,
    name,
    description,
    conversations=None,
    user_id="",
    tenant_id="",
    csf_id=""
):
    if conversations is None:
        conversations = []

    return {
        "auth": {
            "locale": "ro-RO",
            "timeZone": -180,
            "timeZoneId": "Europe/Bucharest"
        },
        "conversationSafeFolder": {
            "id": csf_id,
            "name": name,
            "description": description,
            "supervisors": [],
            "conversations": conversations,
            "userId": user_id,
            "tenantId": tenant_id,

            # 🔵 folder mode
            "addConversations": False,
            "removeConversations": False,
            "exportFolders": False,
            "allowedInPolicy": False,
            "isCaseManagement": False,

            "visibilityDetails": {
                "visibilityDetailsActive": False,
                "visibilityDetailsTranscript": True,
                "visibilityDetailsAnalytics": True,
                "visibilityDetailsAnalyticsChange": True,
                "visibilityDetailsMetadata": True,
                "visibilityDetailsTTL": True,
                "visibilityDetailsCustomFields": True,
                "visibilityDetailsNotes": True,
                "visibilityDetailsReplay": True,
                "visibilityDetailsQM": True,
                "visibilityCleanUp": True,
                "visibilityExport": True
            }
        }
    }

DEFAULT_ADD_RECORD_TO_FOLDER_PARAMS = {
    "name": TEST_FOLDER_NAME,
    "description": TEST_FOLDER_DESCRIPTION,
    "conversations": [],
    "user_id": "",
    "tenant_id": "",
    "csf_id": ""
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

# Default parameters for bulk export input
DEFAULT_BULK_EXPORT_PARAMS = {
    "list_id": [],
    "zip_password": TEST_RECORD_EXPORT_ZIP_ID,
    "bulk_name": TEST_RECORD_EXPORT_ZIP_NAME,
    "only_transcript": False,
    "only_metadata": False,
    "include_mail_body": True,
    "include_mail_attachments": True
}