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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCIsImtpZCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc1MjA4OTQyLCJuYmYiOjE3NzUyMDg5NDIsImV4cCI6MTc3NTIxMjg0MiwiYWlvIjoiQVNRQTIvOGJBQUFBYXBoampBM3lxcCt0ZTdIUHhJTDZzNTdTM0VIa3lVZzF3ZlQvTHgzSThmZz0iLCJhcHBpZCI6IjczZmFkMTdjLThkZmUtNGZkYi04NDEzLTc0ZjE2YzNmN2QwYSIsImFwcGlkYWNyIjoiMSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzQ0Nzk2MzE2LWYxYWMtNDI3YS04YWI5LTI1N2FlZDAyYTUzMS8iLCJvaWQiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJyaCI6IjEuQVVjQUZtTjVSS3p4ZWtLS3VTVjY3UUtsTVMwN3p6LUVmdzlCaWhNSFh0Zk9qQjRBQUFCSEFBLiIsInJvbGVzIjpbImFjY2Vzc19hc19hcHAiXSwic3ViIjoiZGY1NjYyMjQtMDdlNi00ZjMwLThiMmYtNmRlZDc5MjEyNzA3IiwidGlkIjoiNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxIiwidXRpIjoiSXlsaG9PY2lmVXl3ejNNWGVUUVhBQSIsInZlciI6IjEuMCIsInhtc19mdGQiOiJhM01nd09lTlE4V2U4MThFbXl0WTVaVndrckpVYnhCWUVLN0FidlM2YVJFQmMzZGxaR1Z1WXkxa2MyMXoifQ.eHv5aTVJIYXax9KNNx1Z84FP8Gv9twlQ45ORu-eE_QAB835o0V_3vQI2AfnBIjZJnNDSGDitOvoEQ5ss0I2jm5POjShacz8Blhz520juO5CTQaVpMspDh0TeAC46H6_11mGYfNsVlXAmmyv7uZrvkWFYhiD0eXJMSeYXpYPN-tgRVfBFhCe_8HxjK_VyCv-KA8VkPhbuGvwCPEYJhlJybuhTKgBvtietibEgSrnx-WG6Nx4tPPzAUR6NjO6eP69YNHdGMdLg1z30je-NDHl68rI1kgCh5ni0d1kwp28s_Qr7CLpnQRFsSSY9KxtO8qwRwfik62J7NTn1GmA0WiYMVw"
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