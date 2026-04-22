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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCIsImtpZCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc2ODYyNDc0LCJuYmYiOjE3NzY4NjI0NzQsImV4cCI6MTc3Njg2NjM3NCwiYWlvIjoiQVNRQTIvOGJBQUFBbDluNm9OY3JxRWRQV1l2cVUvM1FGYVlyc00xYlFOL0JGVEV2ZGRBZUVnWT0iLCJhcHBpZCI6IjczZmFkMTdjLThkZmUtNGZkYi04NDEzLTc0ZjE2YzNmN2QwYSIsImFwcGlkYWNyIjoiMSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzQ0Nzk2MzE2LWYxYWMtNDI3YS04YWI5LTI1N2FlZDAyYTUzMS8iLCJvaWQiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJyaCI6IjEuQVVjQUZtTjVSS3p4ZWtLS3VTVjY3UUtsTVMwN3p6LUVmdzlCaWhNSFh0Zk9qQjRBQUFCSEFBLiIsInJvbGVzIjpbImFjY2Vzc19hc19hcHAiXSwic3ViIjoiZGY1NjYyMjQtMDdlNi00ZjMwLThiMmYtNmRlZDc5MjEyNzA3IiwidGlkIjoiNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxIiwidXRpIjoia0tUX1YycFkzMEs0Tm9TQlh2NGRBQSIsInZlciI6IjEuMCIsInhtc19mdGQiOiJ2M0dzWnJXMUg4c2tmQ0hsN01vMklXYlVxVXpudGZnbE9UbGF5T1E4Z1BvQlpYVnliM0JsYm05eWRHZ3RaSE50Y3cifQ.icL9AOqXsa5PIpic75Xu0k5-qhaB93TOpDOQkeZJsB83bdFczmDVvkRHJm7a6vaZPJMTXdVOGLG0d9uPtx9GPoV3t84QtSlQiAaxU5I1nWZy48xQIm4rsGuhvuOEnx6oHSGKlcgQ9jrho2N9VIW6j2dZr_ugAeIWOHoioglYnaUjLeM35juzLnmoYYmVfTkMBMq_v9S1X270gYcA8pHY3xn5pB-vPpnaDsgVwU1x2LkxOeDdnuRiCxye-45stWg_rU6kh2m20zhDedD5jq4c1xvqKp21Z5n0MiV8fBVSpVfPq7yyK3Hu6oFnSRK_JxUg1rcRKc3llM0I92wHNZNZPw"
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