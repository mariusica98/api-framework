# config/graphql_client_no_token.py
import requests
from config.graphql_client import GraphQLClient

class GraphQLClientNoToken(GraphQLClient):
    def __init__(self, env_name="Stage", config_file="env-config.json"):
        super().__init__(env_name, config_file)
        self.token = None  

    def execute(self, query, variables=None):
        headers = {"Content-Type": "application/json"}
        payload = {"query": query}
        if variables:
            payload["variables"] = variables

        response = requests.post(self.endpoint, json=payload, headers=headers)
        
        return response