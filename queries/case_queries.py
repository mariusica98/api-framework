CREATE_CASE_MUTATION = """
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

DELETE_CASE_MUTATION = """
mutation deleteCSFolder($conversationSafeFolder: String!) {
  deleteConversationSafeFolder(id: $conversationSafeFolder) {
    status
    __typename
  }
}
"""

GET_CASE_BY_ID_QUERY = """
query getConversationSafeFolder($id: String, $auth: AuthInput) {
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

GET_ALL_CASES_QUERY = """
query getAllCSFolders($auth: AuthInput, $filter: String) {
  getConversationSafeFolders(input: $auth, filter: $filter) {
    id
    name
    description
    isCaseManagement
  }
}
"""
