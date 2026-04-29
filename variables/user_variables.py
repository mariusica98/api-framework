
# Functions to build input data for users operations
def build_update_user_input(
    *,
    user_id,
    recording_rules=None,
    access=None,
    license=None,
    addOnAnalytics=None,
    addOnCaseManagement=None,
    addOnCompliance=None,
    addOnDynamics=None,
    addOnEmail=None,
    addOnFullChat=None,
    addOnGenesys=None,
    addOnLeapXpert=None,
    addOnMsftTeamsUC=None,
    addOnMsftTeamsVoice=None,
    addOnQualityManagement=None,
    addOnRingcentral=None,
    addOnZoom=None,
):
    user_obj = {
        "id": user_id,
        "recordingRules": recording_rules,
        "access": access,
        "license": license,
        "addOnAnalytics": addOnAnalytics,
        "addOnCaseManagement": addOnCaseManagement,
        "addOnCompliance": addOnCompliance,
        "addOnDynamics": addOnDynamics,
        "addOnEmail": addOnEmail,
        "addOnFullChat": addOnFullChat,
        "addOnGenesys": addOnGenesys,
        "addOnLeapXpert": addOnLeapXpert,
        "addOnMsftTeamsUC": addOnMsftTeamsUC,
        "addOnMsftTeamsVoice": addOnMsftTeamsVoice,
        "addOnQualityManagement": addOnQualityManagement,
        "addOnRingcentral": addOnRingcentral,
        "addOnZoom": addOnZoom,
    }

    user_obj = {k: v for k, v in user_obj.items() if v is not None}

    return {
        "auth": DEFAULT_AUTH,
        "user": [user_obj]
    }

def build_create_user_input(
    *,
    user_id,
    name,
    username,
    license
):
    user_obj = {
        "userId": user_id,
        "name": name,
        "username": username,
        "license": license
    }

    user_obj = {k: v for k, v in user_obj.items() if v is not None}

    return {
        "auth": DEFAULT_AUTH,
        "user": [user_obj]
    }

#  Default parameters for updating a user input
DEFAULT_AUTH = {
    "locale": "ro-RO",
    "timeZone": -180,
    "timeZoneId": "Europe/Bucharest"
}

DEFAULT_USER_UPDATE_PARAMS = {
    "addOnAnalytics": True,
    "addOnCaseManagement": True,
    "addOnCompliance": True,
    "addOnDynamics": False,
    "addOnEmail": True,
    "addOnFullChat": True,
    "addOnGenesys": False,
    "addOnLeapXpert": False,
    "addOnMsftTeamsUC": False,
    "addOnMsftTeamsVoice": False,
    "addOnQualityManagement": True,
    "addOnRingcentral": False,
    "addOnZoom": False,
}