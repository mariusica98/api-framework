import requests

class GraphQLClient:
    def __init__(self, env_name="T03"):
        self.env_name = env_name

        self.endpoint = f"https://dev{env_name.lower()}-graph.asc-recording.dev/graphql"

        # Token Bruno - needs to be changed when expired untill we have a proper auth flow in place
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCIsImtpZCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc0ODc2MzA2LCJuYmYiOjE3NzQ4NzYzMDYsImV4cCI6MTc3NDg4MDIwNiwiYWlvIjoiazJaZ1lEaTM5WjJVTm9kZm1OY0pzd1d2OXg2TzVlWmRsbEtWY2w1UnVPdXlnSy9aNzk4QSIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiJfa1p3WVBYNDIwU3ZBX2xLN080TUFBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6IlBUNnQzeldmUmJacU91bjZ5U0lMbHVWN2dtNEZqVWJERmxqTnRZLXg5WThCYzNkbFpHVnVZeTFrYzIxeiJ9.cwcdVXi8Rf5SSCpbeQridN9RaLne7-joOZ9NG6Pb7M7MPg3B2dJ1-4Y4FuWs_dh9RM9rBktLxpvLw7XDP5nvM34wxuG6ofjSz64cIVYjflsXubn9hG1YJDUDt4GqIsBUEd20lIyiuOBLHPztGzRq-DdhWM4Z9kQHHHHXOpxx_8Re-iBXKYH0k_Rcb4EK4EI0OuF7dhK2HmxLGZ1k8tbdvZfGah2eoDkEQ5kNP6ZuOVAVo3p3uM-Z0WcalD3Pv13wdOuZ7D5xddKPqritfLmYjRQWk07ri16lpofgWH8pbPW3Bp_qWobRAC5C0MqKj9GDZaYl-LTRhlLvsQEzYSGXsw"

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