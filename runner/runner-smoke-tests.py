import pytest

tests_to_run = [
    "tests/cases/test_add_case.py",
    "tests/cases/test_get_case.py"
]

if __name__ == "__main__":
    pytest.main(tests_to_run + ["-v", "-s", "--alluredir=allure-results"])