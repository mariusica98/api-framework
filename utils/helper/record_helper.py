
from queries.record_queries import *

class RecordHelper:
    """
    Helper class for managing Records via GraphQL.
    Includes create, get by id, and delete operations.
    """
    def __init__(self, client):
        self.client = client

    def add_record_to_csf(self, input_data):
        """
        Adds a conversation (record) to an existing case.
        """
        response = self.client.execute(ADD_RECORD_TO_CSF_MUTATION, input_data)
        return response["data"]["createConversationSafeFolder"]
    
    def add_record_to_case_bulk(self, input_data):
        response = self.client.execute(
            BULK_CASE_MANAGEMENT_MUTATION,
            input_data
        )
        return response["data"]["bulkCaseManagementMutation"]

    def add_record_to_folder_bulk(self, input_data):
        response = self.client.execute(
            ADD_RECORD_TO_FOLDER_BULK_MUTATION,
            input_data
        )
        return response["data"]["bulkCoversationSafe"]

    def remove_record_from_case(self, input_data):
        """
        Removes a conversation (record) from an existing case.
        """
        response = self.client.execute(REMOVE_RECORD_FROM_CASE_MUTATION, input_data)
        return response["data"]["bulkCaseManagementMutation"]

    def remove_record_from_folder(self, input_data):
        response = self.client.execute(
            REMOVE_RECORD_FROM_FOLDER_MUTATION,
            input_data
        )
        return response["data"]["bulkCoversationSafe"]

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
    
    def generate_jwt_token_for_call(self, input_data):
        """
        Generates JWT token for a call and returns the token string.
        """
        response = self.client.execute(
            GENERATE_JWT_TOKEN_QUERY,
            input_data
        )

        return response["data"]["generateJWTTokenForCall"]
    
    def get_entry_with_jwt(self, input_data):
        """
        Retrieves entry using JWT token.
        """
        response = self.client.execute(
            GET_ENTRY_WITH_JWT_QUERY,
            input_data
        )

        return response["data"]["getEntryWithJWT"]