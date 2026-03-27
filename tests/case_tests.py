import pytest
from utils.graphql_client import GraphQLClient
from queries.case_queries import CREATE_CASE_MUTATION
from variables.case_variables import create_case_input


@pytest.fixture(scope="module")
def client():
    return GraphQLClient()   # folosește implicit env_name="T03"


def test_create_case(client):
    response = client.execute(CREATE_CASE_MUTATION, create_case_input)
    case_folder = response["data"]["createConversationSafeFolder"]

    # salvăm ID-ul pentru alte teste dacă e nevoie
    pytest.case_id = case_folder["id"]

    assert isinstance(case_folder["id"], str) and case_folder["id"] != ""
    assert case_folder["status"] == "ok"