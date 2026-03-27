import requests

class GraphQLClient:
    def __init__(self, env_name="T03"):
        self.env_name = env_name

        self.endpoint = f"https://dev{env_name.lower()}-graph.asc-recording.dev/graphql"

        # Token Bruno - needs to be changed when expired untill we have a proper auth flow in place
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCIsImtpZCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc0NjE3NzI5LCJuYmYiOjE3NzQ2MTc3MjksImV4cCI6MTc3NDYyMTYyOSwiYWlvIjoiQVNRQTIvOGJBQUFBK28rbmgrNEpZbEhqS3piN01xVGp4ODJneFova2ROSnQ0c01XTlpXZEdmQT0iLCJhcHBpZCI6IjczZmFkMTdjLThkZmUtNGZkYi04NDEzLTc0ZjE2YzNmN2QwYSIsImFwcGlkYWNyIjoiMSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzQ0Nzk2MzE2LWYxYWMtNDI3YS04YWI5LTI1N2FlZDAyYTUzMS8iLCJvaWQiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJyaCI6IjEuQVVjQUZtTjVSS3p4ZWtLS3VTVjY3UUtsTVMwN3p6LUVmdzlCaWhNSFh0Zk9qQjRBQUFCSEFBLiIsInJvbGVzIjpbImFjY2Vzc19hc19hcHAiXSwic3ViIjoiZGY1NjYyMjQtMDdlNi00ZjMwLThiMmYtNmRlZDc5MjEyNzA3IiwidGlkIjoiNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxIiwidXRpIjoiUVFUOEpQbUhqRXlxa3VmZUVfVWNBQSIsInZlciI6IjEuMCIsInhtc19mdGQiOiJJME5TdnF0dGJCVmZxcmtuc1gtYTh5Uk4zUWZQblRaWTBjSHBMRDhWM1VVQmMzZGxaR1Z1WXkxa2MyMXoifQ.hs-po9twwFA_odG8NbecgMxa7NX11AGa_xinKAs4_Dz9zjBAItuB07rQlxNB59C0_qAJN6-ErsJ3wclk5T2qGRJ5637GnPDf4f2cCR11gL6c8TMq7hZLEfFBurybkWqDgt7g_M1QtfZv1PDfdClwgRfMckNDJ8W1F7vZEnYypIPJKVSKSqRiuq4eB5H0w6j2m0qoVN2GZPN0Z_BrPFkaFrZEmtcrp_JW1wvPmZKlrD_mPAy6HObhe7O0TCIu3vknoTuFm6XLMi3JAUUvQw2O9PU9j5N_NLsMBxvC8emNxAjXUfHjvacm_FjjZCShnyYvMs4V3ShiMz6Xxkl7IBzRKA"

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