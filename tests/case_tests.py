import pytest
from utils.graphql_client import GraphQLClient
from queries.case_queries import CREATE_CASE_MUTATION
from variables.case_variables import create_case_input

@pytest.fixture(scope="module")
def client():
    return GraphQLClient() 

class TestCaseFlow:

    def test_create_case(self, client):
        """
        The test verifies the Case creation.
        """
        response = client.execute(CREATE_CASE_MUTATION, create_case_input)
        case_folder = response["data"]["createConversationSafeFolder"]

        assert isinstance(case_folder["id"], str) and case_folder["id"] != "", \
            f"Expected a non-empty string for 'id', but got: {case_folder['id']!r}"

        assert case_folder["status"] == "ok", \
            f"Expected status 'ok', but got: {case_folder['status']!r}"

        assert case_folder["text"] == "", \
            f"Expected text to be empty string '', but got: {case_folder['text']!r}"