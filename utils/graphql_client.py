import requests

class GraphQLClient:
    def __init__(self, env_name="T03"):
        self.env_name = env_name

        self.endpoint = f"https://dev{env_name.lower()}-graph.asc-recording.dev/graphql"

        # tokenul rămâne EXACT cum este
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCIsImtpZCI6IlFaZ045SHFOa0dORU00R2VLY3pEMDJQY1Z2NCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc0NjEzNDQ0LCJuYmYiOjE3NzQ2MTM0NDQsImV4cCI6MTc3NDYxNzM0NCwiYWlvIjoiQVNRQTIvOGJBQUFBVGhqSE9kSG9kQkp2SmVSU2tsT3JROUxwaTd2QXJtK3BIMkpRcmZSNzBsQT0iLCJhcHBpZCI6IjczZmFkMTdjLThkZmUtNGZkYi04NDEzLTc0ZjE2YzNmN2QwYSIsImFwcGlkYWNyIjoiMSIsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzQ0Nzk2MzE2LWYxYWMtNDI3YS04YWI5LTI1N2FlZDAyYTUzMS8iLCJvaWQiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJyaCI6IjEuQVVjQUZtTjVSS3p4ZWtLS3VTVjY3UUtsTVMwN3p6LUVmdzlCaWhNSFh0Zk9qQjRBQUFCSEFBLiIsInJvbGVzIjpbImFjY2Vzc19hc19hcHAiXSwic3ViIjoiZGY1NjYyMjQtMDdlNi00ZjMwLThiMmYtNmRlZDc5MjEyNzA3IiwidGlkIjoiNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxIiwidXRpIjoic2dPbUdKZ3kxa1dReHp4UnFZOEVBQSIsInZlciI6IjEuMCIsInhtc19mdGQiOiJ5R1ZFdjVBMkNVZU8yckxSTDNzYkdON3lqRVRfeVlEZmNIeld1d2NRdzN3QlpYVnliM0JsZDJWemRDMWtjMjF6In0.Dpfru4PBvYJIs1ntKBGKKQmg0PUzt5b6QZvUYtfE4Dfhf3sSTX5ZZeTNFm_6ZM0xc9FSisyjIwI1FtrcC6nQU3ejWu8necl8GqPPf4lQbbwpL6gLGz5Weut4kEQ34nYeXnnwKhKqy749-59Q7uBnhu47LNwfa-gJxTGwZ92o_tKZma_uvy_OH2vGUiu7yFl01nsVPaxubvKvbgKBRDU2W-0NwpdEhDrX5u0xQGk77h4FdbXW_0sCS-_2sxgdTuoX1henhFl12pAnCDxtFslGqQMOgtQYqJAbYzewrsrmErhvACBNz2GwxzhpQvTvqOOwIsfDMaHXfIAULMB5IKM-QA"

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