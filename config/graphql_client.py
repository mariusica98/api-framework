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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCIsImtpZCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc2ODQ4NTQ1LCJuYmYiOjE3NzY4NDg1NDUsImV4cCI6MTc3Njg1MjQ0NSwiYWlvIjoiazJaZ1lIajBWVk85ZWFFTVgwWkR4cFlYQ3NzMkhIelV2S1A3alVpdjBGckJOS2JTWnh3QSIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiJ2SjJobTN4NUZrNk02bFp2VV9rQUFBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6InM5cGp2Wm5ERllrYUE5eTY1YVY2Z2tXZ0tzbVBYRVJQTWFLYl93NlVWNlFCWlhWeWIzQmxkMlZ6ZEMxa2MyMXoifQ.qT_lvf0POSu374jfAkcRpjRjxirXTD6PmEiECzkm0RXKC9OGPwREXPeZDpZZ4VfxIvXx8PkExX6RFNIJP2DldjwQMF4WJeuFkKGF-CplAREyquO7XRq7wzjbIdMsgTyVM4onaNnPj3M2K3n3padEgQ-2oEDJDpLmnN7cJ6I-7b6O_l8M_jzjx4Mx6o1bK5WCxn8QKL3rArHz0eOKOKfH2IqMUFiAy-jEzF55zJYOC1ceQyffuUjdzk2TRK7sOCs3F0LAghNu3b2sPtAio68M8IQvVP4GX-e36mLbHqFtB8wMTFaTQeR_eB2Psy1APNK0JKpINqGcTCwz86sOex-AQQ"
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