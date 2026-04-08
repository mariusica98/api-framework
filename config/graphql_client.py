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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCIsImtpZCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc1NjM1MzgyLCJuYmYiOjE3NzU2MzUzODIsImV4cCI6MTc3NTYzOTI4MiwiYWlvIjoiazJaZ1lPQ2ZrYmJoVE9TenQ1RUxmVFo2OVBROEV3NDN1RkdSRWZseFA3TnA0eHpaZDd3QSIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiJhTHlfbmtsXzFreU82U0IwY1NrNkFBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6InZ1Vl9zYjNhdnZ0N1hWbm5rcUtiWlUzTlFTaEUxQzNMLU5oYkZMM3lxa3NCWm5KaGJtTmxZeTFrYzIxeiJ9.gmZcCaOZ1K9PHT7aH51GfhBm1TfmfOc9T5ouk8NoWa7p21nhi3kQzpWdRPFCjIxYIMOe9gfgmejbresYPOR67bVKmYR6KTLLTaX1Buo0aypAhQulzcriycchzxC8r7Ct_Ai0OBlxY_1BCHwesscjjxpEBJjSXaih54b3_K4IXmaLm2iGsdgsNnNLL3x34Lm2Tp_dFbHqqbH3MrJ0gqk9MEWYzXfhSolqz2xyGnadpvHwviBMQKXnXaxRk-A0OkLiWIHZgmxtxlcsFlsKbEsfStdUP7yxd-57LIybag1iUu1wvN9QHMAjgQL-fDx3IRoK_aZsI0KRHHL57KATZ4ZDpA"
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