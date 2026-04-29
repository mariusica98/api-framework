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

# DELETE USER MUTATION
DELETE_USER_MUTATION = """
mutation ent($auth: AuthInput, $id: [String]) {
  deleteUser(input: $auth, id: $id) {
    id
    name
    __typename
  }
}
"""

# GET CONFIG DATA
GET_CONFIG_DATA_QUERY = """
query ent($auth: AuthInput) {
  getConfigData(input: $auth) {
    userdata {
      id
      userId
      name
      username
    }
  }
}
"""