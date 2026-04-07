from queries.report_queries import *
from variables.report_variables import *

class ReportHelper:
    """
    Helper class for managing Reports via GraphQL.
    Includes create operation for now.
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

    def delete_report_by_id(self, report_id):
        """
        Deletes a report by its ID.
        """
        if not report_id:
            return "skipped", None

        variables = build_delete_report_by_id_input(report_id=report_id)
        response = self.client.execute(DELETE_REPORT_BY_ID_MUTATION, variables)
        result = response["data"].get("deleteReport")

        if result is None or "id" not in result:
            raise Exception(f"Failed to delete report {report_id}, response: {response}")

        deleted_id = result["id"]
        typename = result.get("__typename")
        return deleted_id, typename