from queries.conversation_safe_folder import *
from variables.conversation_safe_variables.case_variables import *

class CaseHelper:
    """
    Helper class for managing Cases via GraphQL.
    Includes create, get by id, and delete operations.
    """
    def __init__(self, client):
        self.client = client
    
    def create_case(self, input_data):
        """
        Creates a Case with the provided input data. Returns the created case object.
        """
        response = self.client.execute(UPSERT_CSF_MUTATION , input_data)
        return response["data"]["createConversationSafeFolder"]

    def get_case_by_id(self, case_id):
        """
        Retrieves a Case by its ID.
        """
        variables = build_get_case_by_id_input(case_id=case_id)
        response = self.client.execute(GET_CSF_BY_ID_QUERY, variables)
        return response["data"]["getConversationSafeFolder"]

    def delete_case_by_id(self, case_id):
        """
        Deletes a Case by its ID.
        """
        if not case_id:
            return "skipped", None

        payload = {"conversationSafeFolder": case_id}
        response = self.client.execute(DELETE_CSF_MUTATION, payload)

        result = response["data"]["deleteConversationSafeFolder"]
        status = result["status"]
        typename = result.get("__typename")

        if status != "ok":
            raise Exception(f"Failed to delete case {case_id}, got status: {status}")

        return status, typename

    def get_all_cases(self, filter="AllItems"):
        """
        Retrieves all cases
        """
        variables = build_get_all_cases_input(filter=filter)
        response = self.client.execute(GET_ALL_CSFS_QUERY, variables)
        return response["data"].get("getConversationSafeFolders", [])
    
    def update_case(self, case_id, update_data):
        """
        Update a case by id
        """
        if update_data is None:
            raise ValueError("update_data must be provided")

        update_data["conversationSafeFolder"]["id"] = case_id
        response = self.client.execute(UPSERT_CSF_MUTATION , update_data)
        return response["data"]["createConversationSafeFolder"]