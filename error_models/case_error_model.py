
from typing import List, Optional
from attr import dataclass

@dataclass
class GetCsfNonExistingIdResponse:
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    addConversations: Optional[List] = None
    removeConversations: Optional[List] = None
    exportFolders: Optional[List] = None
    supervisors: List = None
    visibilityDetails: Optional[dict] = None
    attentionRequired: Optional[bool] = None
    conversations: List = None
    ownerName: Optional[str] = None
    userId: Optional[str] = None
    tenantId: Optional[str] = None
    allowedInPolicy: bool = False
    allowedToEditFlagAllowedInPolicy: bool = False
    isCaseManagement: bool = False
    caseManagementDetails: Optional[dict] = None

@dataclass
class GraphQLErrorExtensions:
    code: Optional[str] = None
    codes: Optional[List[str]] = None
    number: Optional[str] = None

@dataclass
class GraphQLError:
    message: Optional[str] = None
    extensions: Optional[GraphQLErrorExtensions] = None

@dataclass
class GraphQLErrorResponse:
    errors: Optional[List[GraphQLError]] = None
    data: Optional[dict] = None 