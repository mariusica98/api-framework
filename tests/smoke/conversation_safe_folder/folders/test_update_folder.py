import pytest
import allure

from config.graphql_client import GraphQLClient
from utils.helper.conversation_safe_folder_helper.folder_helper import FolderHelper
from utils.test_data import TEST_FOLDER_DESCRIPTION_UPDATED, TEST_FOLDER_NAME_UPDATED, TEST_TENANT_ID, TEST_USER_ID
from variables.conversation_safe_variables.folder_variables import DEFAULT_FOLDER_INPUT_PARAMS, build_create_folder_input, build_update_folder_input

@pytest.fixture(scope="module")
def client():
    return GraphQLClient()


@pytest.fixture(scope="module")
def folder_helper(client):
    return FolderHelper(client)

@pytest.fixture
def cleanup_context(folder_helper):
    context = {
        "folder_id": None
    }

    yield context

    with allure.step("Cleanup: deleting created folder"):
        if context["folder_id"]:
            folder_helper.delete_folder_by_id(context["folder_id"])

class TestUpdateFolderFlow:

    @allure.feature("Folder Management")
    @allure.title("Update Folder successfully")
    def test_update_folder(self, folder_helper, cleanup_context):

        # --- Input for folder creation ---
        create_input = build_create_folder_input(**DEFAULT_FOLDER_INPUT_PARAMS)

        # --- Create folder ---
        with allure.step("Creating folder"):
            folder = folder_helper.create_folder(create_input)
            folder_id = folder["id"]
            cleanup_context["folder_id"] = folder_id

        # --- Input for update folder ---
        with allure.step("Preparing update data"):
            update_input = build_update_folder_input(
                folder_id=folder_id,
                name=TEST_FOLDER_NAME_UPDATED,
                description=TEST_FOLDER_DESCRIPTION_UPDATED,
                export_folders=True,
                user_id=TEST_USER_ID,
                tenant_id=TEST_TENANT_ID
            )

        # --- Update folder ---
        with allure.step("Updating folder"):
            folder_helper.update_folder(update_input)

        # --- Get updated folder ---
        with allure.step("Getting folder by id"):
            updated_folder = folder_helper.get_conversation_safe_folder_by_id(folder_id)

        # --- Assertions for updated folder ---
        with allure.step("Verify updated data"):
            assert updated_folder["id"] == folder_id
            assert updated_folder["name"] == TEST_FOLDER_NAME_UPDATED
            assert updated_folder["description"] == TEST_FOLDER_DESCRIPTION_UPDATED