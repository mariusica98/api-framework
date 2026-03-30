import requests

class GraphQLClient:
    def __init__(self, env_name="T03"):
        self.env_name = env_name

        self.endpoint = f"https://dev{env_name.lower()}-graph.asc-recording.dev/graphql"

        # Token Bruno - needs to be changed when expired untill we have a proper auth flow in place
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCIsImtpZCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc0ODYzNzgxLCJuYmYiOjE3NzQ4NjM3ODEsImV4cCI6MTc3NDg2NzY4MSwiYWlvIjoiazJaZ1lORGNkZmFUekxHVFYvdTFYT0txTkNWM2ZWSnZzUEZ5WG5GV1YxdXhLdmhDMWpjQSIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiJTblhHNGJ4VTcwVzBxd1U4VjFKVkFBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6ImlOWXFrRHVyUU1GX1hqUW1IUEhUMGZIR2tRUlhSN3E3OTR1Y19GS2VhMmdCWm5KaGJtTmxZeTFrYzIxeiJ9.hI0uETEAc9vkrjCQC2SN5XUhwV1W-J8tdn_SyXtGnnVbDEQhOB9riLXZyoLjuyjmFeKhcH43WatGI2PHfqgJFsqvIU-97Prm4gaJ3zbfta4r8xfTSzKpl5qwPNNBuu8m_vL4ndg2BH0o6F8mKcawCAoc9nAkzHhSbgG6UGm9ivnvzGFbIBZXOBdj1UZMXap620QGTGrbAqvOfIZoqVuxUzCMEnCYjeC7GAgi-QdeY0Pr7JrbGLKGgXs5IYxJguVuJ4dyNHibJGsFioKD8KWL70mVC3_ZktiR3d6SdbkORHdeX0weViAbfn-a5lV1yXoAuWAyJMC_1gsZZaKb1IhSmg"

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