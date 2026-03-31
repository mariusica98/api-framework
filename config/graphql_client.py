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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCIsImtpZCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc0OTM2MjMxLCJuYmYiOjE3NzQ5MzYyMzEsImV4cCI6MTc3NDk0MDEzMSwiYWlvIjoiQVNRQTIvOGJBQUFBbXF2eWRyOXVPRXltSWJwWDR2blA4ejc2aXZFQTFwSHByRU1oaTBhYTRCdz0iLCJhcHBpZCI6IjczZmFkMTdjLThkZmUtNGZkYi04NDEzLTc0ZjE2YzNmN2QwYSIsImFwcGlkYWNyIjoiMSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzQ0Nzk2MzE2LWYxYWMtNDI3YS04YWI5LTI1N2FlZDAyYTUzMS8iLCJvaWQiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJyaCI6IjEuQVVjQUZtTjVSS3p4ZWtLS3VTVjY3UUtsTVMwN3p6LUVmdzlCaWhNSFh0Zk9qQjRBQUFCSEFBLiIsInJvbGVzIjpbImFjY2Vzc19hc19hcHAiXSwic3ViIjoiZGY1NjYyMjQtMDdlNi00ZjMwLThiMmYtNmRlZDc5MjEyNzA3IiwidGlkIjoiNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxIiwidXRpIjoiZ2huRGc1QkFjVS12dlk1ZjZ0b25BQSIsInZlciI6IjEuMCIsInhtc19mdGQiOiJlOUUwdHpsVlpQUDZNTnJNM3pRTWRfMF9Tc01wM2V2YWtYM2lWYllWb1JJQlpYVnliM0JsZDJWemRDMWtjMjF6In0.TzD3weaBsEoL4ff_ijL599fPz1VcZN8Ss28UMJQk7VX6o8GvcxoyL3hWuV4M5YDh-UWTWu9_Q-E1uLxT8h8DCDTrfgR0ngm28pWxUZU1H1dRw6LI0NK6r3VclnYFRKYU0O0902Gb1nNznaPViE4tzikvGDuq0PJX_aj-nHFVRvuCtd71V190p0pRb8mzpa6Nwvf7x-gmzuOQe8WjnoeyBKNyMurtNC_dQinz9PFfr_W9sgu1rSaWjyS3udOPEMA3UE2d2Hjd6i3y_Y91hT8qxm2QUnPcsCjkOmaUctQA-qOvnGNtVpRBlYmh8HHrx_fK-xYMDGELMGY6hHJkDjEMqA"
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