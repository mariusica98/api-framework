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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCIsImtpZCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc1NDgxMjg4LCJuYmYiOjE3NzU0ODEyODgsImV4cCI6MTc3NTQ4NTE4OCwiYWlvIjoiazJaZ1lCRHVXYmM4S1dlYnpKM0FkczUzWGwwbjgwb3RmM281ZmxZejNyWFc1Y20wMzljQiIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiI1bUc5TE1wZWhrbVNPZU56NkFNTkFBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6IkVwczFlTG9KQWRDaHp3NnZRQUhFQnNjN0JqUXpKWVpKdUR0U05BNFptUzhCWlhWeWIzQmxibTl5ZEdndFpITnRjdyJ9.c1ZL29_i32NzpWcQC_8I9kcWRhJQ09Z_oAFZKfmM6pxSrlYDLY3A7o-Eybw4RNGCPdXCACU3z3pcU4DgAaYrT7bzyuQjMZCoLqKeP62ouLpoiqHiTommdEuuiknyivSvCvKz70GflRpU5gHQVBeRJJQdQghOs8djZCOhBPau_BqI2mRzAcFL7-BhYeBevCIw18ZMV3FQdJ9hk0oB9NaoNz8C4U3_bhl29hLz8MsNQ6WdHSGxXgbkzgeixXBC6CLshL3JpMeMqlLMCej204Q5TTXEsRUIsZlu7l_Ou_wsuenm8mKFaeF8rv2bjQctQw8Oi1SjQQicLo5r2twqQYFazw"
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