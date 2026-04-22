
# Functions to build input data for folder operations
from utils.test_data import *


def build_create_folder_input(
    *,
    name,
    description,
    user_id,
    tenant_id,
    conversations=None
):
    if conversations is None:
        conversations = []

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
            "addConversations": False,
            "removeConversations": False,
            "exportFolders": False,
            "allowedInPolicy": False,
            "isCaseManagement": False
        }
    }

def build_delete_folder_input(*, folder_id):
    return {
        "conversationSafeFolder": folder_id
    }

def build_get_folder_by_id_input(*, folder_id):
    return {
        "id": folder_id,
        "auth": {
            "locale": "ro-RO",
            "timeZone": -180,
            "timeZoneId": "Europe/Bucharest"
        }
    }

# Default parameters for creating a folder input
DEFAULT_FOLDER_INPUT_PARAMS = {
    "name": TEST_FOLDER_NAME,
    "description": TEST_FOLDER_DESCRIPTION,
    "user_id": "",
    "tenant_id": ""
}