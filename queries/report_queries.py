# CREATE REPORT QUERYS
CREATE_REPORT_MUTATION = """
mutation ent(
  $input: AuthInput
  $id: String
  $title: String
  $kpi: String
  $keyword: String
  $sortOrder: Int
  $widget: String
  $cycle: String
  $startDate: DateTime
  $endDate: DateTime
  $person: [PersonInputType]
  $type: String
  $tenantId: String
  $valueType: String
  $tForm: String
  $alarming: AlarmingInputType
  $categories: String
  $reportSend: Boolean
  $jobType: JobInputType
  $reportMail: String
  $botAppId: String
  $jobId: String
  $dashboard: String
  $conversationType: [String]
  $emailAttachmentFormat: String
  $problemTypes: [String]
  $pstnNumber: String
  $dtmfStartDate: DateTime
  $dtmfEndDate: DateTime
) {
  createReport(
    input: $input
    report: {
      id: $id
      title: $title
      kpi: $kpi
      keywords: $keyword
      sortOrder: $sortOrder
      widget: $widget
      cycle: $cycle
      startDate: $startDate
      endDate: $endDate
      persons: $person
      type: $type
      tenantId: $tenantId
      valueType: $valueType
      tForm: $tForm
      alarming: $alarming
      categories: $categories
      reportSend: $reportSend
      jobType: $jobType
      reportMail: $reportMail
      botAppId: $botAppId
      jobId: $jobId
      dashboard: $dashboard
      conversationType: $conversationType
      emailAttachmentFormat: $emailAttachmentFormat
      problemTypes: $problemTypes
      pstnNumber: $pstnNumber
      dtmfStartDate: $dtmfStartDate
      dtmfEndDate: $dtmfEndDate
    }
  ) {
    id
  }
}
"""

# DELETE REPORT BY ID QUERY
DELETE_REPORT_BY_ID_MUTATION = """
mutation ent($input: AuthInput, $id: String!) {
  deleteReport(input: $input, id: $id) {
    id
    __typename
  }
}
"""