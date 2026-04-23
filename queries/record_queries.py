
# ADD RECORD TO CASE QUERIES
ADD_RECORD_TO_CSF_MUTATION = """
mutation ent(
  $auth: AuthInput!
  $conversationSafeFolder: ConversationSafeFolderInputType!
) {
  createConversationSafeFolder(
    input: $auth
    conversationSafeFolder: $conversationSafeFolder
  ) {
    id
    text
    status
  }
}
"""

# REMOVE RECORD FROM CASE QUERY
REMOVE_RECORD_FROM_CASE_MUTATION = """
mutation bulkCaseManagementMutation(
  $auth: AuthInput,
  $conversationId: [String],
  $selectedFolders: [String],
  $action: String,
  $riskRating: String
) {
  bulkCaseManagementMutation(
    input: $auth,
    conversationId: $conversationId,
    selectedFolders: $selectedFolders,
    action: $action,
    riskRating: $riskRating
  ) {
    status
  }
}
"""

# EXPORT RECORD QUERIES
BULK_EXPORT_RECORDS_MUTATION = """
mutation ent(
  $auth: AuthInput,
  $listId: [String]!,
  $zipPassword: String,
  $bulkName: String,
  $onlyTranscript: Boolean,
  $onlyMetadata: Boolean,
  $includeMailBody: Boolean,
  $includeMailAttachemnts: Boolean
) {
  bulkExport(
    input: $auth,
    listId: $listId,
    zipPassword: $zipPassword,
    bulkName: $bulkName,
    onlyTranscript: $onlyTranscript,
    onlyMetadata: $onlyMetadata,
    includeMailBody: $includeMailBody,
    includeMailAttachemnts: $includeMailAttachemnts
  )
}
"""

# GET RECORD BY ID QUERY
GET_RECORD_BY_ID_QUERY = """
query ent($id: ID!, $auth: AuthInput, $callStartMs: String, $isHistoryVault: Boolean) {
  getEntry(input: $auth, id: $id, callStartMs: $callStartMs, isHistoryVault: $isHistoryVault) {
    id
    conversationId
    topic
    duration
  }
}
"""

# GET ALL RECORDS QUERY
GET_ALL_RECORDS_QUERY = """
query getFilterRecordings(
  $val: String!,
  $filter: RecordingFilterInputType,
  $withSave: Boolean,
  $auth: AuthInput,
  $path: String,
  $searchIn: [String]
) {
  getFilterRecordings(
    search: $val,
    filter: $filter,
    withSave: $withSave,
    input: $auth,
    path: $path,
    searchIn: $searchIn
  ) {
    days {
      date
      content {
        id
        conversationId
        topic
        duration
      }
    }
  }
}
"""