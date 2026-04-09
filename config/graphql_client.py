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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCIsImtpZCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc1NzE4NjUwLCJuYmYiOjE3NzU3MTg2NTAsImV4cCI6MTc3NTcyMjU1MCwiYWlvIjoiazJaZ1lPaXJEejU4NWhabitOSDZiRGM5QnZtWXdpbmQ1cXN6M2dmTzdUbHc4aDN6ekY0QSIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiJqZ090N2tXNG4wbWRyMG91MU1FUUFBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6IlZnMDI2SVNHTHh6VmkwYW5heV9SX2tUNjBFMER1T0swd0owd0l6Vmc1R2dCWlhWeWIzQmxkMlZ6ZEMxa2MyMXoifQ.LAMMJ_-BvFSN900w6ZyNrLEXaA6TooZ4IPflZ4m8qgIAHxVUJnTHVlXGSAmUBkEMXCZZqNI_dfJDiK_qO3zW_lunSm-c8hMI7sax-pw4Du8plOYjz33g52DuZSotc0bq4O-IMhKp8cPkYelLU_JCUmfHWuQcm97_g9UsSiEopHKCD5-DB8y92RlmN0iwPXqBGkvpBkjIIB_6dcBv4ad0M34eR16_wkz-C7IUZXTXwtloUS2UUkO8yVPELhqzEnf6FKyuZNGSrjytP93FKUogESTiYzcv7_rC9MKGG7qrSYwMVc24qsTfJq3dSnlcBYQxVaa_bd4Xz7E-Yj5YDyIOUA"
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