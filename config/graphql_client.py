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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCIsImtpZCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc2ODU2NTI0LCJuYmYiOjE3NzY4NTY1MjQsImV4cCI6MTc3Njg2MDQyNCwiYWlvIjoiazJaZ1lHRHZjTGhZL0padGIvd2EvOTVNODdlNVhnb2NoeHVPVEpLNThHZWVtT2RhblhJQSIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiJGMmZaT09mNkNFS2JzY1pMNUVRUEFBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6ImsxS3pkQnI3V1lxRWFwS0EwUk8yZk1aQzRNeVBLMmtPeFVpRVFHOGJRakFCWm5KaGJtTmxZeTFrYzIxeiJ9.h5s1diMnt0VQ9tsAlkO1iQkxTweD8exiZorB4bYrsKncmzZS0EWHqlPQ1TUU4Ko5rGRs86YFvA1v1QJF1RV-_ARCvvdSwc_FBaV1l_tS_3mfPyhdneDxTT5qOr9dAl-x7Vv8O_DrK44Tl8afXCiRisH3SNtuvpl5UjC4gTRmv620O4E8MNUJObp6AWNUBXMvqFxVkeO6nRPx4ZPUdz_1V1m2WX4aM5z8CGHvekDF9bH9WP0W9H7xyTeN6uX5OApkeVmH7qSDdkRcyWNfDywzn2griCNCNWbhIX9Xp4q8whETLI3Y3KAvQZ510v6N3MhJKb_CVIgDmCqejDPy0d6Z3w"
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