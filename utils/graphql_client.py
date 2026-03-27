# utils/graphql_client.py
import requests

class GraphQLClient:
    def __init__(self, env_name="T03"):
        self.endpoint = "https://devt03-graph.asc-recording.dev/graphql"
        # Tokenul copiat din Bruno
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCIsImtpZCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc0NjA5MDgzLCJuYmYiOjE3NzQ2MDkwODMsImV4cCI6MTc3NDYxMjk4MywiYWlvIjoiazJaZ1lEaTM5WjJVTm9kZm1OY0pzd1d2OXg2TzVlWmRsbEtWY2w1UnVPdXlnSy9aNzk4QSIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiJpVzUteDdYbW1FeWV0SkowUmg4WUFBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6InFxV2JVeUREVFBORUN6ZDFJSmFadmxuMnhaNmhFUmRudTZGRldJaDJwTmNCWlhWeWIzQmxibTl5ZEdndFpITnRjdyJ9.gqT_EED3500ApYNFyVDqTwWVPITpuugWD51nRs9_f7KcPDhh9dJfy_IPX6kD_fbGX4cuN6o0LUPzB2c_SbmGyZJyr3Wbj7MHDkN1h8h1omDK3RgLU9saLujyEV5tWrTFMnqqVFXTrfkaCxjB7KG2ZOwipZNzknd6cBB3v7GPZd6RuVq7oyCZIm13E682v_gXQp3-DomjBecuc2CEKQTbFNegW-kMtZj7dYWC8edPog8lFxsQUV2sMwtyZF-Wl25HBJ8EQPd_CMwll-fMatBQBTnhnzyoFeA7yhW6UIgm2h3Ug8K4y0ugTsrKaP7pchdUsFzXhQkvfN_Nqott8FaeVQ"

    def execute(self, query, variables=None):
        """
        Trimite cerere GraphQL către endpoint
        """
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