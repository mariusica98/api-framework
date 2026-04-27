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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCIsImtpZCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc3MjgxNjQyLCJuYmYiOjE3NzcyODE2NDIsImV4cCI6MTc3NzI4NTU0MiwiYWlvIjoiQVNRQTIvOGJBQUFBWE5McUlPMmM2ZFVDdmZXS3NXVTAzWENjYmFoOGRKMXd5N3AwWUp3YjF1WT0iLCJhcHBpZCI6IjczZmFkMTdjLThkZmUtNGZkYi04NDEzLTc0ZjE2YzNmN2QwYSIsImFwcGlkYWNyIjoiMSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzQ0Nzk2MzE2LWYxYWMtNDI3YS04YWI5LTI1N2FlZDAyYTUzMS8iLCJvaWQiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJyaCI6IjEuQVVjQUZtTjVSS3p4ZWtLS3VTVjY3UUtsTVMwN3p6LUVmdzlCaWhNSFh0Zk9qQjRBQUFCSEFBLiIsInJvbGVzIjpbImFjY2Vzc19hc19hcHAiXSwic3ViIjoiZGY1NjYyMjQtMDdlNi00ZjMwLThiMmYtNmRlZDc5MjEyNzA3IiwidGlkIjoiNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxIiwidXRpIjoiMTRuSEtBWVVMVWltODg4WFFEQlNBQSIsInZlciI6IjEuMCIsInhtc19mdGQiOiJCMW85SEZYQXVhWjV5ZnRvVFA0YkpGT0kzd1pxUVp3dTdPWV8zeWplRnVzQmMzZGxaR1Z1WXkxa2MyMXoifQ.J7SuU1xEbNPmEQ0VzfU61bdoX4lHBz4NL6OHctnxLUM-STZC77605oA_FuJmtxsFcJWewwGj2VU9WJMWJsFT8imBAX-f84VVDd3xOmiu3_xUdJSZh3E3MFZJPMpDtEf30-GvA38L_RyU-ocnDygSk9DM0y_RK91U2oyPVuP_TK4AbSnHKUwa7cf7RmqAOzTCW59xi7qlAOeYM8pBCLGiVt9_e13tD1hzws5xyR2lEpjUb_OQzsTLPuomZeauVkGV4CJqe9D5VhrCcl3h6B8L6p102HppWB6eelhXD_BaolJatarM19t0LFtBDWZGGv7aiM90xDiNBexN4uniiC9dPA"
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