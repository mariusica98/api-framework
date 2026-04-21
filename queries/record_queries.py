
# ADD RECORD TO CASE QUERIES
ADD_RECORD_TO_CASE_MUTATION = """
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