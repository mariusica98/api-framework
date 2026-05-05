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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ilh0LW83aERicHVwQXotWlBtNkh4Q0ZXUzNjSSIsImtpZCI6Ilh0LW83aERicHVwQXotWlBtNkh4Q0ZXUzNjSSJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc3OTc4Njc3LCJuYmYiOjE3Nzc5Nzg2NzcsImV4cCI6MTc3Nzk4MjU3NywiYWlvIjoiazJGZ1lQamNXYmU5VDVuaGFaYTgwWnJIeWRNMTVPNDBwZk1jTmJ5YmtqZTViZjVTUVdFQSIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiJGaDI0U2dLTzVFQ3Q1TE1iZ1VCU0FBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6IjRYVEc3NWNlLXM1ckw3TFJjbnNmbmh3b2stbWhab0l3d0VxaFFwOERmN3dCWlhWeWIzQmxibTl5ZEdndFpITnRjdyJ9.nvmwMqma2Mxpy_SagA2xiufiWRQoDmNlZfDVcVQj5rcLRED14MyKzxFbyRqFU-qEixZy4LFhOorHpGGejepKnwmdMp0BJlVdmD4u7sGoZ0A9SCDopJWVqbcZ_xfeN_L1OYI9J7-TwgRZa_PDJEI8khVl3521om57ChB5bG03WKHl6OmCyLZSCTr7fqgiQ70GHj4H9t4QyKauXvMbUBjHRfZGdshClBMRsdDE4o2Zw9Pei3L1-srkjFMMuekYJyU0ael1ygb0bAhMATzoTiD8It-VE0JcJqrt_XSHKrZpDBS9Nqc1lEhdxxm5ms0lhoFgnL4z--Uv4dt4D7Gc_hAquQ"
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