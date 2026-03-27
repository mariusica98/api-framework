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