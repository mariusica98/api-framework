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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCIsImtpZCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc1NTUwNzc1LCJuYmYiOjE3NzU1NTA3NzUsImV4cCI6MTc3NTU1NDY3NSwiYWlvIjoiQVNRQTIvOGJBQUFBYXBoampBM3lxcCt0ZTdIUHhJTDZzNTdTM0VIa3lVZzF3ZlQvTHgzSThmZz0iLCJhcHBpZCI6IjczZmFkMTdjLThkZmUtNGZkYi04NDEzLTc0ZjE2YzNmN2QwYSIsImFwcGlkYWNyIjoiMSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzQ0Nzk2MzE2LWYxYWMtNDI3YS04YWI5LTI1N2FlZDAyYTUzMS8iLCJvaWQiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJyaCI6IjEuQVVjQUZtTjVSS3p4ZWtLS3VTVjY3UUtsTVMwN3p6LUVmdzlCaWhNSFh0Zk9qQjRBQUFCSEFBLiIsInJvbGVzIjpbImFjY2Vzc19hc19hcHAiXSwic3ViIjoiZGY1NjYyMjQtMDdlNi00ZjMwLThiMmYtNmRlZDc5MjEyNzA3IiwidGlkIjoiNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxIiwidXRpIjoiNXFncXZoMndNRW1tWFpuWDNoUUdBQSIsInZlciI6IjEuMCIsInhtc19mdGQiOiJmNm1ibHR2ZVJ6UEJTQkEydEJBVlVfcXJVZmtDVHp0bXFnRmlOR3NqLTBRQlpYVnliM0JsYm05eWRHZ3RaSE50Y3cifQ.S7RflPrEpXUmnOHZ_C9cY7xHLRfQQ9K3NBQGNiPrrwEh9eY0n1IyUmFg7Hmr1xz5LiiWhVKVWAhh7e2YoC1EeeiIQGebYMAvXGynfdmHJ4weT8sbC9cHQ54gTVfZTyKRwANopsi_YaC6NWPCcTRASKQBxqSqDGDZAiS88ebu20lmluhTVMYKafnZ9_OE0J2zrQBYol6G7bVi8T6kcvfG18O9JepVR5V5IXUucsQ69WmkBxDwr3N9fkGg7yrbj3EGtqoQrFUsHM7ENcNB_wL_Pm5xkBxhJVYc6f6IEiOiaMHZ37b4NT89NwV9MMewZbczh6eu2BVPWKCLbR98Ee7b3g"
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