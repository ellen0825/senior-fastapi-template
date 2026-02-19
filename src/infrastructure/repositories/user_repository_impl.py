from uuid import UUID
from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):

    def __init__(self):
        self.storage = {}

    def save(self, user: User) -> None:
        self.storage[str(user.id)] = user

    def get_by_id(self, user_id: UUID) -> User | None:
        return self.storage.get(str(user_id))