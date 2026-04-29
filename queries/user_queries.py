# UPDATE USER MUTATION
UPDATE_USER_MUTATION = """
mutation ent($auth: AuthInput, $user: [UserDataInput]) {
  updateUser(input: $auth, user: $user) {
    name
    __typename
  }
}
"""