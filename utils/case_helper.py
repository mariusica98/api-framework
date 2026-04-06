from queries.case_queries import *
from variables.case_variables import *

class CaseHelper:
    """
    Helper class for managing Cases via GraphQL.
    Includes create, get by id, and delete operations.
    """
    def __init__(self, client):
        self.client = client

    def create_case(self, input_data=None):
        """
        Creates a Case. Returns the created case object.
        """
        if input_data is None:
            input_data = CREATE_CASE_INPUT
        response = self.client.execute(CREATE_CASE_MUTATION, input_data)
        return response["data"]["createConversationSafeFolder"]

    def get_case_by_id(self, case_id):
        """
        Retrieves a Case by its ID. Returns the case data.
        """
        variables = GET_CASE_BY_ID_INPUT.copy()
        variables["id"] = case_id
        response = self.client.execute(GET_CASE_BY_ID_QUERY, variables)
        return response["data"]["getConversationSafeFolder"]

    def delete_case_by_id(self, case_id):
        """
        Deletes a Case by its ID.
        """
        if not case_id:
            return "skipped", None

        payload = {"conversationSafeFolder": case_id}
        response = self.client.execute(DELETE_CASE_MUTATION, payload)

        result = response["data"]["deleteConversationSafeFolder"]
        status = result["status"]
        typename = result.get("__typename")

        if status != "ok":
            raise Exception(f"Failed to delete case {case_id}, got status: {status}")

        return status, typename

    def get_all_cases(self, filter="AllItems"):
        """
        Retrieves all cases.
        """
        variables = {
            "auth": {
                "locale": "ro-RO",
                "timeZone": -120,
                "timeZoneId": "Europe/Bucharest"
            },
            "filter": filter
        }
        response = self.client.execute(GET_ALL_CASES_QUERY, variables)
        return response["data"].get("getConversationSafeFolders", [])
    
    def update_case(self, case_id, update_data=None):
        """ 
        Updates a Case by id.
        """
        if update_data is None:
            update_data = UPDATE_CASE_INPUT.copy()

        update_data["conversationSafeFolder"]["id"] = case_id
        response = self.client.execute(UPDATE_CASE_MUTATION, update_data)

        return response["data"]["createConversationSafeFolder"]