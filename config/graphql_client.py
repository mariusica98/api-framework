import requests

class GraphQLClient:
    def __init__(self, env_name="T03"):
        self.env_name = env_name

        self.endpoint = f"https://dev{env_name.lower()}-graph.asc-recording.dev/graphql"

        # Token Bruno - needs to be changed when expired untill we have a proper auth flow in place
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCIsImtpZCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc0ODU3NjQwLCJuYmYiOjE3NzQ4NTc2NDAsImV4cCI6MTc3NDg2MTU0MCwiYWlvIjoiQVNRQTIvOGJBQUFBMGNlR1BncTFSUDZINUs4QWZTQ3g3dldseEY3SHorMkIwZ3dyeGt0WkxCQT0iLCJhcHBpZCI6IjczZmFkMTdjLThkZmUtNGZkYi04NDEzLTc0ZjE2YzNmN2QwYSIsImFwcGlkYWNyIjoiMSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzQ0Nzk2MzE2LWYxYWMtNDI3YS04YWI5LTI1N2FlZDAyYTUzMS8iLCJvaWQiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJyaCI6IjEuQVVjQUZtTjVSS3p4ZWtLS3VTVjY3UUtsTVMwN3p6LUVmdzlCaWhNSFh0Zk9qQjRBQUFCSEFBLiIsInJvbGVzIjpbImFjY2Vzc19hc19hcHAiXSwic3ViIjoiZGY1NjYyMjQtMDdlNi00ZjMwLThiMmYtNmRlZDc5MjEyNzA3IiwidGlkIjoiNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxIiwidXRpIjoiLW9VXy1lWGxfMHE5Tm5uMGhYcFRBQSIsInZlciI6IjEuMCIsInhtc19mdGQiOiJ4UTUwekc4TDNoNTZTaG56Qmt0N1FXRVc2Qm5XUE9uZWRSdTBha2xSU0lFQlpuSmhibU5sWXkxa2MyMXoifQ.BE5Nn5gJJ6PcODmorURt7ib580o1SBTo6wkB-zwvlnaWF6Bhh6cQqE6ziIIlQiIAeQNkfOi_hfHo9qTWzEHvBVogdgjxCRuzRKTwxPomviGIBmujHe7sIrMueD2o1ISAVZqsbjatVIE4tcM3tv1yesH4NWmbZL96lFHF7BGUP_acDWibP52tU_v90va-uL_OO7tEBmBW-AuMMFdXIbHM8g5QElFq04Mp-t1qRz5yppuqVehhgL38IsndbDk6b1gsclted6bEgPu8-VTVDIxPlYwoVOdFZPg0E-Jph6cByOxA955GvQWR2zuaUwLFf5LFbOSkpBYgDjW3oGhQpqWsnA"

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