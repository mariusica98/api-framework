
# Functions to build input data for users operations
def build_update_user_input(
    *,
    user_id,

    # Core config
    recording_rules=None,
    replay=None,
    access=None,
    analytics=None,
    storageId=None,
    license=None,

    # Add-ons (feature toggles)
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

        # Core config
        "recordingRules": recording_rules,
        "replay": replay,
        "access": access,
        "analytics": analytics,
        "storageId": storageId,
        "license": license,

        # Add-ons
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

    # Eliminăm câmpurile nefolosite
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

def build_delete_user_input(*, user_id):
    return {
        "auth": DEFAULT_AUTH,
        "id": [user_id]
    }

#  Default parameters for updating a user input
DEFAULT_AUTH = {
    "locale": "ro-RO",
    "timeZone": -180,
    "timeZoneId": "Europe/Bucharest"
}
