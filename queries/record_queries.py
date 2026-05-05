
# ADD RECORD TO CASE QUERIES - CSF
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

# ADD RECORD TO CASE QUERIES - BULK: RECORD PAGE
BULK_CASE_MANAGEMENT_MUTATION = """
mutation bulkCaseManagementMutation(
  $auth: AuthInput,
  $conversationId: [String],
  $selectedFolders: [String],
  $action: String,
  $riskRating: String
) {
  bulkCaseManagementMutation(
    input: $auth
    conversationId: $conversationId
    selectedFolders: $selectedFolders
    action: $action
    riskRating: $riskRating
  ) {
    status
  }
}
"""

# ADD RECORD TO FOLDER QUERIES - BULK: RECORD PAGE
ADD_RECORD_TO_FOLDER_BULK_MUTATION = """
mutation bulkFoldersMutation(
  $auth: AuthInput,
  $conversationId: [String],
  $selectedFolders: [String],
  $action: String
) {
  bulkCoversationSafe(
    input: $auth
    conversationId: $conversationId
    selectedFolders: $selectedFolders
    action: $action
  ) {
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

# REMOVE RECORD FROM FOLDER QUERY
REMOVE_RECORD_FROM_FOLDER_MUTATION = """
mutation bulkFoldersMutation(
  $auth: AuthInput,
  $conversationId: [String],
  $selectedFolders: [String],
  $action: String
) {
  bulkCoversationSafe(
    input: $auth,
    conversationId: $conversationId,
    selectedFolders: $selectedFolders,
    action: $action
  ) {
    status
  }
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

# GET RECORD SHARED TOKEN
GENERATE_JWT_TOKEN_QUERY = """
query ent(
  $input: AuthInput
  $conversationId: String
  $tenantId: String
  $expirationDate: Date
  $withAudio: Boolean
  $withVideo: Boolean
  $withChat: Boolean
  $withTranscript: Boolean
  $withMetadata: Boolean
  $withNotes: Boolean
) {
  generateJWTTokenForCall(
    input: $input
    conversationId: $conversationId
    tenantId: $tenantId
    expirationDate: $expirationDate
    withAudio: $withAudio
    withVideo: $withVideo
    withChat: $withChat
    withTranscript: $withTranscript
    withMetadata: $withMetadata
    withNotes: $withNotes
  )
}
"""

# GET SHARED RECORD PROPERTIES
GET_ENTRY_WITH_JWT_QUERY = """
query ent($jwtToken: String, $callStartMs: String) {
  getEntryWithJWT(jwtToken: $jwtToken, callStartMs: $callStartMs) {
    id
    conversationId
    callStartMs
    callEndMs
    topic
    duration
    tenantId
    hasAudio
    hasVideo
    hasChat
    __typename
  }
}
"""