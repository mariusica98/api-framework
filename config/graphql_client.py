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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCIsImtpZCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc3NTM3NzY2LCJuYmYiOjE3Nzc1Mzc3NjYsImV4cCI6MTc3NzU0MTY2NiwiYWlvIjoiazJaZ1lOaWxJelhiUnM5NzVlYlhoVnQ2OVgweUEzVXZDL25jOUxETzIrcnQ5ZlRnOXRrQSIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiIyanhETm1nX3EwR2NOVGV0bGZNMkFBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6Ik5vUkpKM19PNTg4c3B2VTk1ZFJKel9rZnZtQmxudkFKemVudmxWRERETmdCWm5KaGJtTmxZeTFrYzIxeiJ9.a-nvpjB8ll2vWssFcaKn4rnbHJqaCCF9wt5yCVUj-33FBKPahyJkS9Qoc-zFEl2LCA8icZOzj980RHC0QreUIHYaI1yhiNXrTSEwv5AWDy-m64czs2KMDfDIHP_lbVJONB3-4-va_pjAzePGmEDqy0cbQuPwFpV6wlN15swc8hMvseVcBig11rRg2OGRCqSs4EE-o9d9dtHlKyf5oRUnmGLxWGCf05swKs5pgydGSVsU2tR93jZ8O7YRE0n5gxow8nCthCbkXne7U86S4ot91hBeud7xq6y7Zj9dPPRxgNlBHctVsZin8AqUK-GTpZSfsEqn1KbofjAxoBYSHZAcSw"
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