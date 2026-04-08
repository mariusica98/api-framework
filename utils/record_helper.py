
from queries.record_queries import ADD_RECORD_TO_CASE_MUTATION

class RecordHelper:
    """
    Helper class for managing Records via GraphQL.
    Includes create, get by id, and delete operations.
    """
    def __init__(self, client):
        self.client = client

    def add_record_to_case(self, input_data):
        """
        Adds a conversation (record) to an existing case.
        """
        response = self.client.execute(ADD_RECORD_TO_CASE_MUTATION, input_data)
        return response["data"]["createConversationSafeFolder"]