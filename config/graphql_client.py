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
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCIsImtpZCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc3MzYwMzgxLCJuYmYiOjE3NzczNjAzODEsImV4cCI6MTc3NzM2NDI4MSwiYWlvIjoiQVNRQTIvOGJBQUFBalh3bmtXYkUrYkNuR3EwRHVsNzNSOTNVOE5FMStzczlDZS9LdElHWnU4az0iLCJhcHBpZCI6IjczZmFkMTdjLThkZmUtNGZkYi04NDEzLTc0ZjE2YzNmN2QwYSIsImFwcGlkYWNyIjoiMSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzQ0Nzk2MzE2LWYxYWMtNDI3YS04YWI5LTI1N2FlZDAyYTUzMS8iLCJvaWQiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJyaCI6IjEuQVVjQUZtTjVSS3p4ZWtLS3VTVjY3UUtsTVMwN3p6LUVmdzlCaWhNSFh0Zk9qQjRBQUFCSEFBLiIsInJvbGVzIjpbImFjY2Vzc19hc19hcHAiXSwic3ViIjoiZGY1NjYyMjQtMDdlNi00ZjMwLThiMmYtNmRlZDc5MjEyNzA3IiwidGlkIjoiNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxIiwidXRpIjoiTnBCaEFWM2Y3RVdUbUtLblhUbEJBQSIsInZlciI6IjEuMCIsInhtc19mdGQiOiJBNG9aMTVMbzd1S2lhV3RwN0wtQ1gtZWE1SFkzbFlXbVgwelNvQ2N5Z2lzQlpYVnliM0JsZDJWemRDMWtjMjF6In0.hY7D6tYeFxJQs7AkDaDVHk-TjOPXAFh3584d8T9IsvR1BbfD7Lvn0Vv11J-m0BqSyHTgy8cHBUT0m_caDOHAH20GV6zzXOEdCgo56swjXLmUOsKGv2SN-GpTqDQmXhbjKPCP7B6tWUAIv2sBcgdGWiS2Nsrkov3Ldr79sMO-tJ_726dkv5wlqe0Rr1wJUDzvZvGaeOVA1Gcu2Puo9ljeNhSG8nDkoQUhejDf_cSEmoyrwBnsSAObowJCS5mLGzItmiXbJkLmvjVatOCZL1e_LRW_Va_d8tnZq_j42aUgvnauk5Mr9sj2qND_QDnzqiEvhUwqDn_yBnJvMB0SWqCB8g"
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