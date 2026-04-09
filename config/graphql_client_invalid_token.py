import requests
from enum import Enum
from config.graphql_client import GraphQLClient


class AuthMode(Enum):
    NO_TOKEN = "no_token"
    EXPIRED_TOKEN = "expired_token"
    INVALID_TOKEN = "invalid_token"
    EMPTY_TOKEN = "empty_token"
    CUSTOM_TOKEN = "custom_token"


class GraphQLClientNoToken(GraphQLClient):
    def __init__(
        self,
        env_name="Stage",
        config_file="env-config.json",
        auth_mode=AuthMode.NO_TOKEN,
        custom_token=None
    ):
        super().__init__(env_name, config_file)
        self.auth_mode = auth_mode
        self.custom_token = custom_token

    def _build_headers(self):
        headers = {"Content-Type": "application/json"}

        if self.auth_mode == AuthMode.NO_TOKEN:
            # Nu adăugăm deloc Authorization
            return headers

        if self.auth_mode == AuthMode.EMPTY_TOKEN:
            headers["Authorization"] = "Bearer "
            return headers

        if self.auth_mode == AuthMode.INVALID_TOKEN:
            headers["Authorization"] = "Bearer invalid_token_123"
            return headers

        if self.auth_mode == AuthMode.EXPIRED_TOKEN:
            headers["Authorization"] = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCIsImtpZCI6IlUxc1g4WUZIUzdaNlZsN1ZITEl6VGVqYnZqMCJ9.eyJhdWQiOiJhcGk6Ly9zdGFnZS10ZWFtcy5hc2MtcmVjb3JkaW5nLmFwcC8zZmNmM2IyZC03Zjg0LTQxMGYtOGExMy0wNzVlZDdjZThjMWUiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEvIiwiaWF0IjoxNzc1NjUyMzc4LCJuYmYiOjE3NzU2NTIzNzgsImV4cCI6MTc3NTY1NjI3OCwiYWlvIjoiazJaZ1lQaXd0ZTc2SDhHTlpndmxWYis3cTluVUsyazkyeU55U3Uyc2dDajd0bVBaMCtVQSIsImFwcGlkIjoiNzNmYWQxN2MtOGRmZS00ZmRiLTg0MTMtNzRmMTZjM2Y3ZDBhIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNDQ3OTYzMTYtZjFhYy00MjdhLThhYjktMjU3YWVkMDJhNTMxLyIsIm9pZCI6ImRmNTY2MjI0LTA3ZTYtNGYzMC04YjJmLTZkZWQ3OTIxMjcwNyIsInJoIjoiMS5BVWNBRm1ONVJLenhla0tLdVNWNjdRS2xNUzA3enotRWZ3OUJpaE1IWHRmT2pCNEFBQUJIQUEuIiwicm9sZXMiOlsiYWNjZXNzX2FzX2FwcCJdLCJzdWIiOiJkZjU2NjIyNC0wN2U2LTRmMzAtOGIyZi02ZGVkNzkyMTI3MDciLCJ0aWQiOiI0NDc5NjMxNi1mMWFjLTQyN2EtOGFiOS0yNTdhZWQwMmE1MzEiLCJ1dGkiOiItV3l6dGlkWmNVNk5uSXJHbXB4aEFBIiwidmVyIjoiMS4wIiwieG1zX2Z0ZCI6IjFPMXQ1akFDRzJiRDFub21GNm15V0dFQWZPMVZ4UU0zR1Y0andyWFNaM29CYzNkbFpHVnVZeTFrYzIxeiJ9.C4-0A5hTuYp9Pt13lzlgHtnqWjXwtbJNDskK_Knx9basPT0l-hvJ0erlWUN0mwCGCUUdNaPE3jf3_fBSLbGqnbxpi-I6z41AOEyVbnhB-7okCJoTrJJVu_JbE-kBHcD2_7ll9hOoIpEPzzU43zmKDZEtgToUN7ezF_URa--ptrPsJl-BIIn4zgwqRlcK4G9wAszcZNeR4dpF8Lm-6HXhnGbKqLFP4NYn_VD_nXq6zCruTgk1yPrRpU4PSPIJmGsNNnwy5IOF3qduKWl36nA0d30hRG01RvngSLYA-U1WDGlTyRsqKAzFVriiNtlGJojN17NW_23NGKYqcruure_AuQ"
            return headers

        if self.auth_mode == AuthMode.CUSTOM_TOKEN and self.custom_token:
            headers["Authorization"] = f"Bearer {self.custom_token}"
            return headers

        return headers

    def execute(self, query, variables=None):
        headers = self._build_headers()
        payload = {"query": query}

        if variables:
            payload["variables"] = variables

        response = requests.post(
            self.endpoint,
            json=payload,
            headers=headers
        )

        return response

    # --- Helper methods pentru schimbare rapidă în teste ---

    def use_no_token(self):
        self.auth_mode = AuthMode.NO_TOKEN

    def use_expired_token(self):
        self.auth_mode = AuthMode.EXPIRED_TOKEN

    def use_invalid_token(self):
        self.auth_mode = AuthMode.INVALID_TOKEN

    def use_empty_token(self):
        self.auth_mode = AuthMode.EMPTY_TOKEN

    def use_custom_token(self, token):
        self.auth_mode = AuthMode.CUSTOM_TOKEN
        self.custom_token = token