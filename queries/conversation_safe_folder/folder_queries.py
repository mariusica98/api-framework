
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