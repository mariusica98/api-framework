import os
import json
import requests

# This class creates a GraphQL client that loads environment configuration from a JSON file and sends GraphQL requests to the specified endpoint.
class GraphQLClient:
    def __init__(self, env_name="T03", config_file="env-config.json"):
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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCIsImtpZCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc1MjE5Mzk1LCJuYmYiOjE3NzUyMTkzOTUsImV4cCI6MTc3NTIyMzI5NSwiYWlvIjoiazJaZ1lGaW5XSDQwa0c5cWpJckNtWVM4Mkt3NmpjakRpWGVhTnRmTEhsMTFVdi9BN0FjQSIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiJmM1RWQ2ZCa2ZrV2Q4Z2ZPbDR3WEFBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6IklGNHdISlZ1YjVEUWQ0NVlIV25RODlSRUNoYWNMMDkzZTJBM0JpMW15SmtCWlhWeWIzQmxibTl5ZEdndFpITnRjdyJ9.GF5W-__Xim4vak1SvRvl0U-EfLgfmO7NSgiFIWzYgR5NP1lJfTXgZ3HRPOwl0zgugf8SX9ZVYbdvJ8fYxi42mL-RqBp_YmDyT-a_m0vEIdBUb9bFMOCLy5IvWVtoAN8v8ndXE8vvjh9seDOI5_IiPiYsAawww0POdGazxu9DA5N3PspJ-pxclc4Wp3Horur0PGRCa_0XR1jru6vuN0gOmeVGVlZI2ovM_cvlUULHkSia_w5pEpjnzX6cWFYV4_LICkYER3TQwxDZ5zLgZ-eG-Nc_CXoogduA_xSmRTUPEgIxKO7TmvguFelElOCv7G6D64nS7AjmJE-ra-JRvn1hCg"
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