from queries.case_queries import DELETE_CASE_MUTATION
from variables.case_variables import delete_case_input

class CleanupHelper:
    
    def __init__(self, client):
        self.client = client

    def delete_case_by_id(self, case_id: str):
        """
        Delete Case by ID. Skips deletion if case_id is None or empty.
        Raises exception if deletion fails.
        """
        if not case_id:
            return "skipped"

        try:
            response = self.client.execute(DELETE_CASE_MUTATION, delete_case_input(case_id))
            status = response["data"]["deleteConversationSafeFolder"]["status"]
            if status != "ok":
                raise Exception(f"Failed to delete case with ID {case_id}, got status: {status}")
            return status
        except Exception as e:
            print(f"[Cleanup Warning] Could not delete case {case_id}: {e}")
            raise