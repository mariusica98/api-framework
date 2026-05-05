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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ilh0LW83aERicHVwQXotWlBtNkh4Q0ZXUzNjSSIsImtpZCI6Ilh0LW83aERicHVwQXotWlBtNkh4Q0ZXUzNjSSJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc3OTY4MjM2LCJuYmYiOjE3Nzc5NjgyMzYsImV4cCI6MTc3Nzk3MjEzNiwiYWlvIjoiQVNRQTIvOGNBQUFBS3NxcnFlNGRhVk1tYy9ISTRHakYreHF2RXN2RGlZMmdPNVZKUThrK1RJMD0iLCJhcHBpZCI6IjczZmFkMTdjLThkZmUtNGZkYi04NDEzLTc0ZjE2YzNmN2QwYSIsImFwcGlkYWNyIjoiMSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzQ0Nzk2MzE2LWYxYWMtNDI3YS04YWI5LTI1N2FlZDAyYTUzMS8iLCJvaWQiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJyaCI6IjEuQVVjQUZtTjVSS3p4ZWtLS3VTVjY3UUtsTVMwN3p6LUVmdzlCaWhNSFh0Zk9qQjRBQUFCSEFBLiIsInJvbGVzIjpbImFjY2Vzc19hc19hcHAiXSwic3ViIjoiZGY1NjYyMjQtMDdlNi00ZjMwLThiMmYtNmRlZDc5MjEyNzA3IiwidGlkIjoiNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxIiwidXRpIjoiRjI0cko1eW02RU9halE0T3lhaEpBQSIsInZlciI6IjEuMCIsInhtc19mdGQiOiJ1dHRGMm1WbGJGQ3Brb2YwTHhMU2hCMk5TcThwei04aC1yTDVlMGRua3VVQmMzZGxaR1Z1WXkxa2MyMXoifQ.meeqqhVArs5-eHD38jfaL2QeaxaOIneHTgd9OUpI5-d4RaO1lXul7raC-wksP1P8oSDf6Gn7zBB-QiUcVOrn_h1NdYwG3q5EqqGKM_mRlDg82D7VgkUDHGnDIovoiNVPO08-S6C-Jc8NNuqowW8rhi6l58p4vHxBh7TRP9gMKbZQm6P6FQTsmVBvgVEkUIDKGaZeiBOaBJ0eDqpstKcc2EONYqtPR7DDCwZ6QV_UnJayn2BYRMl-jwckxH6SiUlvVBP-4XgAc1jXNuwkyRIfxofVA3H7Ek8EymTV3HRO89V5ilxRSQB4UNCjDl0GYYBW_uZcCmP2hb4x7G8WnCXYkw"
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