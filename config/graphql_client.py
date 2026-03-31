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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCIsImtpZCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc0OTQ5NzQ3LCJuYmYiOjE3NzQ5NDk3NDcsImV4cCI6MTc3NDk1MzY0NywiYWlvIjoiazJaZ1lIajBWVk85ZWFFTVgwWkR4cFlYQ3NzMkhIelV2S1A3alVpdjBGckJOS2JTWnh3QSIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiJPVklMR0hpTlVrYTY4WlBNS1poakFBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6InhMM3NQM2FMV19rSUJNa3JERkVkanRtOVdERUJTemtRbV9DZHBoWDZQeGdCWlhWeWIzQmxibTl5ZEdndFpITnRjdyJ9.RlCzy26hnBKvJXHoKcIaEmCOmxawOqaCPwzL8YTUSN7hUASRSD9yS-P--FQDCHkTghB2HNqFvJVN8p-2J_-9S_LQAUJCPkHEOm9luuimgquU5uvy2_ZWLxfJza6eaMrBdRkEXqbW0BBHE2txF8ekFaPj9M3KTegymD-k8cVy3F8jEhk-lB9a7LHhs5738IFNYv-934MRFNQwFT4GFQtXFOzZ27MPjTzLvism-lQR2y6IDExIb30JuWwp1VqyDwaDc433J5tjSvS9g9QzZeSjdkCHoerZP5Kn7E115JevPnfYNR0PEMH-wRYSoWKly3U-eRxbqzv_p3u55KdjK2x9cQ"
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