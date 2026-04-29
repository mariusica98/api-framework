# CREATE USER MUTATION
CREATE_USER_MUTATION = """
mutation ent($auth: AuthInput, $user: [UserDataInput]) {
  createUser(input: $auth, user: $user) {
    name
    access
    __typename
  }
}
"""

# UPDATE USER MUTATION
UPDATE_USER_MUTATION = """
mutation ent($auth: AuthInput, $user: [UserDataInput]) {
  updateUser(input: $auth, user: $user) {
    name
    __typename
  }
}
"""