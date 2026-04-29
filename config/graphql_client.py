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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCIsImtpZCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc3NDQxMDE0LCJuYmYiOjE3Nzc0NDEwMTQsImV4cCI6MTc3NzQ0NDkxNCwiYWlvIjoiazJaZ1lQQitFalRQZGtuNjVlY2Q5L3o5YjJYRkh1RnNPeWtUMGUzYmE3djd2OVJQTXhFQSIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiJ0blBaTlZReXZFV3BQb1JmRUQ4UkFBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6IkNtOUMxSjFqSkNub1hDZ1hKZGd5UUx2Q1hWbXp5ZHdXRUJvNlFuaXB2bkFCWlhWeWIzQmxkMlZ6ZEMxa2MyMXoifQ.jz23t1rR4sgpTD2kjrUBG2CNq-IyFyk95qh9dDSug6wg_ieMUrI_XO-4kFXTkhzpvcRJlPYRNtzhNFm1YaXPwv2q8htUii1VgLj-yGs5ygi1RHrCI8NjdQsORyuf0Un5MUMJxQ4oEbDamRP2opa2FIvR9aAI_KHStuOGjq9_iAjVn9KSyskN0_XqORnSHnzyFrIC3KtcvWCAOmSIAEp4L0SNRNd5QREBsygjGlyb9Oa10qpnT9RYMzkQ9YTXEWGtXhhqFizJZlLln6lhiWzBmGNUf5GuMxwefqTp9i9Bbi3yfPlP8GkAvNzwPEmLAgBzzEqr5HdRcXdo9p6CWEtXBQ"
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