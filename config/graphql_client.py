import os
import json
import requests

# This class creates a GraphQL client that loads environment configuration from a JSON file and sends GraphQL requests to the specified endpoint.
class GraphQLClient:
    def __init__(self, env_name="Stage", config_file="env-config.json"):
        self.env_name = env_name

        # Get the directory where this file is located
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir, config_file)

        # Load configuration
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file does not exist: {config_path}")

        with open(config_path, "r") as f:
            config = json.load(f)

        # Get environment configuration
        env_config = config.get(env_name)
        if not env_config:
            raise ValueError(f"No configuration found for environment {env_name}")

        self.endpoint = env_config["endpoint"]

        # Token
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCIsImtpZCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc1NjUyMzc4LCJuYmYiOjE3NzU2NTIzNzgsImV4cCI6MTc3NTY1NjI3OCwiYWlvIjoiazJaZ1lQaXd0ZTc2SDhHTlpndmxWYis3cTluVUsyazkyeU55U3Uyc2dDajd0bVBaMCtVQSIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiItV3l6dGlkWmNVNk5uSXJHbXB4aEFBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6IjFPMXQ1akFDRzJiRDFub21GNm15V0dFQWZPMVZ4UU0zR1Y0andyWFNaM29CYzNkbFpHVnVZeTFrYzIxeiJ9.C4-0A5hTuYp9Pt13lzlgHtnqWjXwtbJNDskK_Knx9basPT0l-hvJ0erlWUN0mwCGCUUdNaPE3jf3_fBSLbGqnbxpi-I6z41AOEyVbnhB-7okCJoTrJJVu_JbE-kBHcD2_7ll9hOoIpEPzzU43zmKDZEtgToUN7ezF_URa--ptrPsJl-BIIn4zgwqRlcK4G9wAszcZNeR4dpF8Lm-6HXhnGbKqLFP4NYn_VD_nXq6zCruTgk1yPrRpU4PSPIJmGsNNnwy5IOF3qduKWl36nA0d30hRG01RvngSLYA-U1WDGlTyRsqKAzFVriiNtlGJojN17NW_23NGKYqcruure_AuQ"
    def execute(self, query, variables=None):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        payload = {"query": query}
        if variables:
            payload["variables"] = variables

        response = requests.post(self.endpoint, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()