import pytest
from config.graphql_client import GraphQLClient
from queries.case_queries import CREATE_CASE_MUTATION
from variables.case_variables import create_case_input
from utils.cleanup_methods import CleanupHelper

@pytest.fixture(scope="module")
def client():
    return GraphQLClient() 

class TestCaseFlow:

    def test_create_case(self, client):
        """
        The test verifies the Case creation.
        """
        case_id = None
        try:
            response = client.execute(CREATE_CASE_MUTATION, create_case_input)
            case_folder = response["data"]["createConversationSafeFolder"]

            case_id = case_folder["id"]

            # Asserts
            assert isinstance(case_id, str) and case_id != "", \
                f"Expected a non-empty string for 'id', but got: {case_id!r}"
            assert case_folder["status"] == "ok", \
                f"Expected status 'ok', but got: {case_folder['status']!r}"
            assert case_folder["text"] == "", \
                f"Expected text to be empty string '', but got: {case_folder['text']!r}"

        finally:
            # Cleanup
            if case_id:
                cleanup = CleanupHelper(client)
                cleanup.delete_case_by_id(case_id)
    
