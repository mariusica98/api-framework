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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCIsImtpZCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc1NzE0NjcyLCJuYmYiOjE3NzU3MTQ2NzIsImV4cCI6MTc3NTcxODU3MiwiYWlvIjoiazJaZ1lPQ01uekE5Ykk2dndlelNzKzk3ZnFpWGJBdlJ2NmEvcklCdDV3TE9qcFhjUmhjQSIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiJ4TVIyU1ItNkVVeWxxbzIwbEZ3SkFBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6ImJha1FHQ2lLY3k1R2Vab0xQX3QycUoySW5RbXhaTS1LLWZwWGNKXzdZcTBCYzNkbFpHVnVZeTFrYzIxeiJ9.A4WkJHcfmqQygeHnOku9UOFp43j_Ea7Z-ha24plqtlGP7LGPJfrmg_vkm5LabVYWJVRJk-euCTozi2QFKrllaojpXmvN8NtUVLfc25RHkv240xrdeTTaL69V3fE4lgLQ8vsBFi78PJDlEs8HeRJWl5s2wyWOrpvpGkMfKTzSb_2Ao0h107KJbCOe5FhKHYlSQTUTCnbFcSD7HFNteaIvIitYul9EpSU0IQegs2KTNlDjulKOIyCKIvG1yhuw4LgD3RIIBp7p88fpQdtrmLFyAjVbM3BLgj8MfoOLTUopI65KMqHENFkTz9Jeg-PRftg_6jH5U5Nf8ihm9RpiZQzXmQ"
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