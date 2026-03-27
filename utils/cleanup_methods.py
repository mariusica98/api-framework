from queries.case_queries import DELETE_CASE_MUTATION
from variables.case_variables import delete_case_input

class CleanupHelper:
    
    def __init__(self, client):
        self.client = client

    def delete_case_by_id(self, case_id: str):
        """
        Delete Case by ID
        """
        response = self.client.execute(DELETE_CASE_MUTATION, delete_case_input(case_id))
        status = response["data"]["deleteConversationSafeFolder"]["status"]
        if status != "ok":
            raise Exception(f"Failed to delete case with ID {case_id}, got status: {status}")
        return status