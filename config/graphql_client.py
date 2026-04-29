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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCIsImtpZCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc3NDY1OTcwLCJuYmYiOjE3Nzc0NjU5NzAsImV4cCI6MTc3NzQ2OTg3MCwiYWlvIjoiazJaZ1lCQlFmR3JZOFhVTzJ6V0hKZUVIMkM3WnFuUWN5bTQ5TTJXN29sREwvdTN0dFU4QiIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiJBZ1U0UFgxcUkwS0VHeEJZZ2hra0FBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6Ijg1RDk1MnNNRDZZSHBIc1Y4VFF6MGNHQ0NzcnBvdVNjaEFZVU9BTmk5NXdCYzNkbFpHVnVZeTFrYzIxeiJ9.P5QEIdGLys85_B7SLFRaT8IxtqqUaIaoptt1GZPkulhxZk-I8__CwltoW89ah55XKJZ7WK_ck9pub8aoe9mCy-6AXfLiQu_xFpyiglCiSY7lmu2CWbBvVU0Zax1Lq7z3YpWorQPQxntXtUR6BPqussr_bRW6xs1toMLPsrmkNLuikhtzC4JUbhiZp7rdgv0iMam5QMWLc348S-XrdJSr6EdCk1QVzMvtAa7MEPIbIGrKJtA5dd05eox0w0ynJrQcIjny6zzBeTN8uMDK7bZAKFqKkjoLkeQ_WQQPa1KobP_i6hRDcCDF_PrzX57AxzYADHDGHP4hppYTxLqO3j3mhg"
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