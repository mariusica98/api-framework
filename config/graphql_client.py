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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCIsImtpZCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc2ODQ0NTM3LCJuYmYiOjE3NzY4NDQ1MzcsImV4cCI6MTc3Njg0ODQzNywiYWlvIjoiazJaZ1lOaTJvVUlpOGZqbjJlOUU2bHhMV3JSTm5rdy9tRnVTMVpQQnBNYW9JeHYvdXhzQSIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiJld3VPck0tUE9VV0FNaDdjUDdjWUFBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6IlZaWmlWMFFZOG1GRnJMbGYxMDdnaFRVLVF1am9mcUVBT0c0VmVJQTZXLW9CWlhWeWIzQmxkMlZ6ZEMxa2MyMXoifQ.lt6-d8b4LPClXlhmodZa8i153zmzfWg3YFY8s9YOTOzCOnvWnW0p5eA2pnDy_zeu06k3mwWA3-iV7zapcfSL6QTg1E_bKtvv-mZYEI4WU4jEnS8ruEU1KiNqNcowV-MOfGT4GHEY5E1K6LfpwiR1OmaeK_IgydHdMbl73WjJz_IGxMj2l6_16cQ_Fu9x-y24xsTxd0jC_Bq0ISc6Zdlu9iaAkXvLFRvC6Fm7eop5GLuvyJrLa9zPde8DIYWwBLEXl71SRA5U1pW730LmH1desspl0tD4oMKs8j7AtWIKXD0-Nqh34HmKs0soxMOkD1y4BNt94Jrk_GjAApDEEnrlfQ"
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