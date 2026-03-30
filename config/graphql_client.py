import requests

class GraphQLClient:
    def __init__(self, env_name="T03"):
        self.env_name = env_name

        self.endpoint = f"https://dev{env_name.lower()}-graph.asc-recording.dev/graphql"

        # Token Bruno - needs to be changed when expired untill we have a proper auth flow in place
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCIsImtpZCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc0ODcyMzc4LCJuYmYiOjE3NzQ4NzIzNzgsImV4cCI6MTc3NDg3NjI3OCwiYWlvIjoiazJaZ1lIQjZZeFFVNC9PSHJkNzg5ODlaVERIYnFwWlZGaVUyVHkxY3F5Y1Y4YlpBMng4QSIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiJjS0tpMDJ5OUowYXBtNXI5Y2dkZUFBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6IlhWRUY5TVY2cEFnZU80WG50VmFSM0hWRk5Ja09OdlI5YmhHVEhDbUNJZzBCYzNkbFpHVnVZeTFrYzIxeiJ9.CCA72Xg9HiUn213fTEx50wol-9EbTMZA_gkl-4T4ZUA21V0sromXHAtSecycyXXinPjPLlGM1X1QuV8RX3IFf-BQl2lZZQTIU7mX1kGrhXwKMmgh9cMCT1u7eJPV5rwqDHawGNWxjhnXZYoFHo2xozyPVDJ0F-E2W1cpK8N4-0xWrqkbuxTvbS2IO5UiOGG7esL0Ig54Yuj4h5Twl4KvML16d6e3-4ChwYgVifIP5FPBJV4p4OLV765fYOfDw4U3epdndi04k7wyCpt3Tkbv4Gx-6k-hIC8gzIRCch5K_W5cfMAH2g7HdNvTt_zPhsYBgj18Bdmij683R0YSaoRvrA"

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