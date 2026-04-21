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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCIsImtpZCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc2NzY4MTI3LCJuYmYiOjE3NzY3NjgxMjcsImV4cCI6MTc3Njc3MjAyNywiYWlvIjoiazJaZ1lCRHRuakUzemZQQnBzQmZINTZhY1g5OE01VS8wMDdIbXp2anU5UEV4WUtLcGxNQiIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiJPQnVvb2JCRGVrVzVYM1RVVUNvc0FBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6IlZCMGdueXpMMm1RM3RsRlo0VDRraWhnRGlMbDlKdmhmM1RSX0piUDFSeVVCYzNkbFpHVnVZeTFrYzIxeiJ9.UvKvcFMd0L8jwf_ZDa1FBaNfaEh8xuLYQwuAUqHgsiEZFq_XzBRpn3VqpHiZjWhVzVZIadHPJI6nlFGe7YTtW1nk5mK4q9D4jN6Adp6_dqWmBicf6Da78uHvCjnSAwh-elE-Y7pV7wLn6ivyMkKqtatIHTfcLp7LnJXBBNt3TwJK7GwYsG2LLuD_V-pJynv8nAlbIZPR6O2Qp-0OiawXw-B7_MY6SaVYf7kd8EnuJkjAvawvu5IUyLWweliOI3oUjlTKtz_o2p_gT7PMnZVXeM-UG8Wd-AHZY51gqZJ4BBcw0l_u8Fs6wHkfoXrik2sinF4lvGWCFJnroFpynN2U2w"
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