import pytest
import allure
from config.graphql_client import GraphQLClient
from utils.helper.conversation_safe_folder_helper.folder_helper import FolderHelper
from variables.conversation_safe_variables.folder_variables import *
from utils.test_data import *


@pytest.fixture(scope="module")
def client():
    return GraphQLClient()


@pytest.fixture(scope="module")
def folder_helper(client):
    return FolderHelper(client)

class TestCreateFolderFlow:

    @allure.feature("Conversation Safe Folder")
    @allure.title("Create Folder successfully")
    def test_create_folder(self, folder_helper):

        folder = None
        folder_id = None
        try:
            # --- Prepare input data ---
            create_input = build_create_folder_input(**DEFAULT_FOLDER_INPUT_PARAMS)

            # --- Create folder ---
            with allure.step("Creating a new folder"):
                folder = folder_helper.create_folder(create_input)
                folder_id = folder["id"]

            # --- Assertions for created folder ---
            with allure.step("Verifying created folder"):
                assert isinstance(folder_id, str) and folder_id != "", \
                    f"Expected non-empty string for id, got: {folder_id!r}"
                assert folder["status"] == "ok", \
                    f"Expected status 'ok', got: {folder['status']!r}"
                assert folder["text"] == "", \
                    f"Expected text to be empty string, got: {folder['text']!r}"

        finally:
            # --- cleanup ---
            with allure.step("Deleting folder"):
                if folder_id:
                    folder_helper.delete_folder_by_id(folder_id)

    @allure.feature("Conversation Safe Folder")
    @allure.title("Create Folder with error - duplicate name")
    def test_create_duplicate_folder(self, folder_helper):

        first_folder = None
        second_folder = None
        first_folder_id = None
        try:
            # --- Input data for the first folder ---
            first_folder_input = build_create_folder_input(**DEFAULT_FOLDER_INPUT_PARAMS)

            # --- Create the first folder ---
            with allure.step("Creating the first folder"):
                first_folder = folder_helper.create_folder(first_folder_input)
                first_folder_id = first_folder["id"]

            # --- Input data for the second folder (same name) ---
            second_folder_input = build_create_folder_input(**DEFAULT_FOLDER_INPUT_PARAMS)

            # --- Create the second folder ---
            with allure.step("Creating a second folder with the same name"):
                second_folder = folder_helper.create_folder(second_folder_input)

            # --- Assertions for duplicate folder ---
            with allure.step("Verifying errors for duplicate folder"):
                assert second_folder["status"] == "error", \
                    f"Expected status 'error' for duplicate folder, got: {second_folder['status']!r}"
                assert second_folder["text"] == "nameDuplicatedError", \
                    f"Expected text 'nameDuplicatedError', got: {second_folder['text']!r}"
                assert second_folder["id"] == "", \
                    f"Expected empty ID for duplicate folder, got: {second_folder['id']!r}"

        finally:
            # --- Cleanup ---
            with allure.step("Deleting the first folder"):
                if first_folder_id:
                    folder_helper.delete_folder_by_id(first_folder_id)
        