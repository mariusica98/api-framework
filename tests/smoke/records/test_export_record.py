import pytest
import allure
from config.graphql_client import *
from utils.case_helper import *
from utils.record_helper import *
from variables.case_variables import *
from utils.test_data import *
from variables.record_variables import DEFAULT_BULK_EXPORT_PARAMS, build_bulk_export_input

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()

@pytest.fixture(scope="module")
def record_helper(client):
    return RecordHelper(client)


class TestBulkExportRecords:

    @allure.feature("Records")
    @allure.title("Bulk export records successfully")
    def test_bulk_export_records(self, record_helper):

         # --- Create input for bulk export ---
        with allure.step("Prepare bulk export input"):
            params = DEFAULT_BULK_EXPORT_PARAMS.copy()
            params.update({
                "list_id": [TEST_RECORD_ID]
            })

            input_data = build_bulk_export_input(**params)

        # --- Execute bulk export mutation ---
        with allure.step("Execute bulk export mutation"):
            response = record_helper.bulk_export_records(input_data)

        # --- Assertions for bulk export response ---
        with allure.step("Verify response"):
            assert response == "" or response is not None