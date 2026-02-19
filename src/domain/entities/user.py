from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class User:
    id: UUID
    email: str
    name: str

    @staticmethod
    def create(email: str, name: str) -> "User":
        return User(id=uuid4(), email=email, name=name)