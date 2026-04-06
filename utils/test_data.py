import uuid

### General user data ###
TEST_TENANT_ID = "44796316-f1ac-427a-8ab9-257aed02a531"
TEST_USER_ID = "32d3161b-f419-4571-8fa4-931fa972f4a8"

### Cases ####
TEST_CASE_NAME_1 = "Test Case using Automation Script"
TEST_CASE_NAME_2 = "Test Case using Automation Script 1"
TEST_CASE_NAME_UPDATED = "Test Case using Automation Script - Updated"
TEST_CASE_DESCRIPTION = "Verifies that a case is created successfully via automation script."
TEST_CASE_DESCRIPTION_UPDATED = "Verifies that a case is updated successfully via automation script."
TEST_INVALID_CASE_ID = str(uuid.uuid4())
TEST_CASE_STATUS_OPEN = "OPEN"
TEST_CASE_STATUS_IN_PROGRESS = "INPROGRESS"
TEST_CASE_CONTENT_STATUS_NEW = "NEW"
TEST_CASE_CONTENT_STATUS_ESCALED = "ESCALATED"
TEST_CASE_RISK_RATING_ADHERANCE = "Adherence"
TEST_CASE_RISK_RATING_INFORMATION = "Info"