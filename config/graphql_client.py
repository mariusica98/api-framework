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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCIsImtpZCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc1NjI2MDI0LCJuYmYiOjE3NzU2MjYwMjQsImV4cCI6MTc3NTYyOTkyNCwiYWlvIjoiQVNRQTIvOGJBQUFBc2YrV1FCZFBPN2tnOUNQbkkyakJPNWp4ZHNtYU9mYUdpZXhqMjJMdnU0cz0iLCJhcHBpZCI6IjczZmFkMTdjLThkZmUtNGZkYi04NDEzLTc0ZjE2YzNmN2QwYSIsImFwcGlkYWNyIjoiMSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzQ0Nzk2MzE2LWYxYWMtNDI3YS04YWI5LTI1N2FlZDAyYTUzMS8iLCJvaWQiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJyaCI6IjEuQVVjQUZtTjVSS3p4ZWtLS3VTVjY3UUtsTVMwN3p6LUVmdzlCaWhNSFh0Zk9qQjRBQUFCSEFBLiIsInJvbGVzIjpbImFjY2Vzc19hc19hcHAiXSwic3ViIjoiZGY1NjYyMjQtMDdlNi00ZjMwLThiMmYtNmRlZDc5MjEyNzA3IiwidGlkIjoiNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxIiwidXRpIjoidTVVanBLN0N5VVdrbV9jbDZwZEpBQSIsInZlciI6IjEuMCIsInhtc19mdGQiOiJBNU0tZ0lyOUlfZVctRVZmMTY1d0NVdXhtWDFreERFek03ZkxvTk5pcC1JQmMzZGxaR1Z1WXkxa2MyMXoifQ.hABLlQnuFwd2sBtSMl-JC8Ax-tbhT9Ot56CfdrJ_h28mh0qOawoj1xSLiwtFeM7THso9q_IS2SlsWZBhBEpxHX8f054yHvxrWr0emcZTXS8vT2L3GyorZQLo8nFNv32vz0SVeYmhMW5nO5nRJajM4SFt1OtzIdhgPLQPibGXVWWJPvzBDH8emvb3z1V9kpFmnPNP2ApjrhA-DXhQXJTaIQaicEuATA-TDxAT9vhFm-ZC9BEdrjwkdvPhdPCoCC-abqs1qV7Z85lNBXE62jZlTRzm2GxosTqmdAvmRAg-vMozg33lBNkzcqlGc3UuE0zqESsZdvSy0UQmF5-zDsGsVQ"
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