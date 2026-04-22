
# CREATE FOLDER MUTATION
CREATE_FOLDER_MUTATION = """
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

# DELETE FOLDER MUTATION
DELETE_FOLDER_MUTATION = """
mutation deleteCSFolder($conversationSafeFolder: String!) {
  deleteConversationSafeFolder(id: $conversationSafeFolder) {
    status
    __typename
  }
}
"""

# GET FOLDER BY ID QUERY
GET_FOLDER_BY_ID_QUERY = """
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

# UPDATE FOLDER MUTATION
UPDATE_FOLDER_MUTATION = """
mutation ent(
  $auth: AuthInput,
  $conversationSafeFolder: ConversationSafeFolderInputType
) {
  createConversationSafeFolder(
    input: $auth,
    conversationSafeFolder: $conversationSafeFolder
  ) {
    id
    text
    status
    __typename
  }
}
"""