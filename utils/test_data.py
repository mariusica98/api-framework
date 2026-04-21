import uuid

### General testing data ###
TEST_API_DASHBOARD_ID = "cd0a2fa0-bae3-e34b-165c-d78f65353b58"

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

### Reports ###
TEST_REPORT_ID = str(uuid.uuid4())
TEST_REPORT_TITLE = "Test Report using Automation Script"
TEST_REPORT_CASE_COMPLIANCE_RATE_KPI = "CaseComplianceRate"
TEST_REPORT_OVERALL_COMPLIANCE_RATE_KPI = "OverallComplianceRate"

### Records ###
TEST_RECORD_ID = "0100b580-eaed-4271-9680-eedade32458f"
TEST_RECORD_INVALID_ID = str(uuid.uuid4())
TEST_RECORD_EXPORT_ZIP_ID = "12345678"
TEST_RECORD_EXPORT_ZIP_NAME = "recordExport"
TEST_RECORD_TOPIC_NAME = "TestUser20 Dev2ASC - Marius Gaitan"
TEST_DEFAULT_RECORDS_PATH = "https://stage-teams.asc-recording.app/"