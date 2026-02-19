from pydantic import BaseModel
from uuid import UUID


class CreateUserRequest(BaseModel):
    email: str
    name: str


class UserResponse(BaseModel):
    id: UUID
    email: str
    name: str