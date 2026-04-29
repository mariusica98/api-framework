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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCIsImtpZCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc3NDQ3Nzg1LCJuYmYiOjE3Nzc0NDc3ODUsImV4cCI6MTc3NzQ1MTY4NSwiYWlvIjoiazJaZ1lPQm52QjBUMXBMK1NzSGo1VDl1TDdjdEI2cllQOTVWbnNuNndhOHd0dUZtY0JrQSIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiJObG5rY2xIa0FFaXBOSmpZQXowVEFBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6InZDT2NYYnhXZ1IwZUhZODZkd2p6djlZTU01TFRBal9obDBwc1VWNHBWaFVCWm5KaGJtTmxZeTFrYzIxeiJ9.LCnBLtnZnRqYXJlWnZPAdyoGhArShCyrhtuu6YLQ_sWIiwl60VoDjgFz7qgLuUEmu9DWgwZfgrlkwGSVS8On6Dp1aMrGU0_Fhl820oqPLMi3ppGE7CCTXQCXbom530JJzqGLtFbfTEA09r9kIBa0hklXnNUZHjas0g6DsafnuCPLF5WXunuw_z8ap5L5EGcDgHERKtPJPq2xq_UlZlJ_2ajmx-qnxZC3B2FCIhgJEE9fBYuQMd62flbNstZnZuqHrcUEj2urwLc6lXwy2uOGEsC3q2o4vmuUVkpD0gibWoTO8xVg8aiGfOGrUQH-1hXyErmkGJcJl0_S2frwGOjFAg"
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