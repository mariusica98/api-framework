import time
import pytest
import shutil
import os
import json

# --- List all tests to run ---
tests_to_run = [
    "tests/smoke/conversation_safe_folder/cases/test_add_case.py",
    "tests/smoke/conversation_safe_folder/cases/test_get_case.py",
    "tests/smoke/conversation_safe_folder/cases/test_delete_case.py",
    "tests/smoke/conversation_safe_folder/cases/test_update_case.py",
    "tests/smoke/conversation_safe_folder/folders/test_add_folder.py",
    "tests/smoke/conversation_safe_folder/folders/test_get_folder.py",
    "tests/smoke/conversation_safe_folder/folders/test_update_folder.py",
    "tests/smoke/conversation_safe_folder/folders/test_delete_folder.py",
    "tests/smoke/reports/test_add_report.py",
    "tests/smoke/records/records_to_case/test_add_record_to_case.py",
    "tests/smoke/records/records_to_case/test_remove_record_to_case.py",
    "tests/smoke/records/records_to_folder/test_add_record_to_folder.py",
    "tests/smoke/records/test_export_record.py",
    "tests/smoke/records/test_get_record.py",
    "tests/security/test_cases_security.py"
]

allure_dir = "allure-results"

# --- Environment variables ---
env_vars = {
    "OS": "Windows 11",
    "Host": "Stage"
}

# --- Allure tests categories ---
categories = [
    {
        "name": "Smoke Tests",
        "matchedTags": ["smoke"]
    }
]

# --- Executor info ---
executor_info = {
    "name": "Local API Tests",
    "type": "pytest",
    "url": "https://stage-graph.asc-recording.app/graphql",
}

if __name__ == "__main__":
    start_time = time.perf_counter()

    # --- Clean the allure-results directory ---
    if os.path.exists(allure_dir):
        shutil.rmtree(allure_dir)
    os.makedirs(allure_dir, exist_ok=True)

    # --- Create environment.properties ---
    with open(os.path.join(allure_dir, "environment.properties"), "w") as f:
        for k, v in env_vars.items():
            f.write(f"{k}={v}\n")

    # --- Create categories.json ---
    with open(os.path.join(allure_dir, "categories.json"), "w") as f:
        json.dump(categories, f, indent=4)

    # --- Create executor.json ---
    with open(os.path.join(allure_dir, "executor.json"), "w") as f:
        json.dump(executor_info, f, indent=4)

    # --- Run tests with pytest and Allure ---
    exit_code = pytest.main(tests_to_run + ["-v", "-s", f"--alluredir={allure_dir}"])

    end_time = time.perf_counter()
    duration = end_time - start_time

    print("\n" + "=" * 50)
    print(f"Total execution time: {duration:.2f} seconds")
    print("=" * 50)
