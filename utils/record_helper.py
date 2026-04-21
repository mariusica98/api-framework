
from queries.record_queries import ADD_RECORD_TO_CASE_MUTATION, BULK_EXPORT_RECORDS_MUTATION, GET_ALL_RECORDS_QUERY, GET_RECORD_BY_ID_QUERY, REMOVE_RECORD_FROM_CASE_MUTATION

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
    
    def remove_record_from_case(self, input_data):
        """
        Removes a conversation (record) from an existing case.
        """
        response = self.client.execute(REMOVE_RECORD_FROM_CASE_MUTATION, input_data)
        return response["data"]["bulkCaseManagementMutation"]

    def bulk_export_records(self, input_data):
        """
        Exports records based on the provided input data.
        """
        response = self.client.execute(BULK_EXPORT_RECORDS_MUTATION, input_data)
        return response["data"]["bulkExport"]
    
    def get_record_by_id(self, input_data):
        """
        Retrieves a record by its ID.
        """
        response = self.client.execute(GET_RECORD_BY_ID_QUERY, input_data)
        return response["data"]["getEntry"]

    def get_all_records(self, input_data):
        response = self.client.execute(GET_ALL_RECORDS_QUERY, input_data)
        return response["data"]["getFilterRecordings"]