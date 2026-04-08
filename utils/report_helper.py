from queries.report_queries import *
from variables.report_variables import *

class ReportHelper:
    """
    Helper class for managing Reports via GraphQL.
    """
    def __init__(self, client):
        self.client = client

    def create_report(self, input_data):
        """
        Creates a Report with the provided input data.
        Returns the created report object.
        """
        response = self.client.execute(CREATE_REPORT_MUTATION, input_data)
        return response["data"]["createReport"]
