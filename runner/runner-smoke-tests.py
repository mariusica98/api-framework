import time
import pytest
import shutil
import os

tests_to_run = [
    "tests/cases/test_add_case.py",
    "tests/cases/test_get_case.py",
    "tests/cases/test_delete_case.py",
    "tests/cases/test_update_case.py"
]

allure_dir = "allure-results"

if __name__ == "__main__":
    start_time = time.perf_counter()

    # --- Cleanup allure-results before each run ---
    if os.path.exists(allure_dir):
        shutil.rmtree(allure_dir)
    os.makedirs(allure_dir, exist_ok=True)

    # --- Run pytest with Allure output ---
    exit_code = pytest.main(tests_to_run + ["-v", "-s", f"--alluredir={allure_dir}"])

    end_time = time.perf_counter()
    duration = end_time - start_time

    print("\n" + "=" * 50)
    print(f"Total execution time: {duration:.2f} seconds")
    print("=" * 50)