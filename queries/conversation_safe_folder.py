# CREATE / EDIT CSF MUTATION
UPSERT_CSF_MUTATION  = """
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

# DELETE CSF MUTATION
DELETE_CSF_MUTATION = """
mutation deleteCSF($conversationSafeFolder: String!) {
  deleteConversationSafeFolder(id: $conversationSafeFolder) {
    status
    __typename
  }
}
"""

# GET CSF BY ID QUERY
GET_CSF_BY_ID_QUERY = """
query getCSF($id: String, $auth: AuthInput) {
  getConversationSafeFolder(id: $id, input: $auth) {
    id
    name
    description
    addConversations
    removeConversations
    exportFolders
    supervisors {
      userId
    }
    visibilityDetails {
      visibilityDetailsActive
      visibilityDetailsNotes
      visibilityDetailsTranscript
      visibilityDetailsTTL
      visibilityDetailsAnalytics
      visibilityDetailsAnalyticsChange
      visibilityDetailsCustomFields
      visibilityDetailsMetadata
      visibilityDetailsReplay
      visibilityDetailsQM
      visibilityCleanUp
      visibilityExport
    }
    attentionRequired
    conversations {
      id
      conversationId
    }
    ownerName
    userId
    tenantId
    allowedInPolicy
    allowedToEditFlagAllowedInPolicy
    isCaseManagement
    caseManagementDetails {
      caseStatus
      contentStatus
      legalHold
      observers
      reviewers
      contentRiskRating
      caseThreadId
    }
  }
}
"""

# GET ALL CSFs QUERY
GET_ALL_CSFS_QUERY = """
query getAllCSFs($auth: AuthInput, $filter: String) {
  getConversationSafeFolders(input: $auth, filter: $filter) {
    id
    name
    description
    isCaseManagement
  }
}
"""
