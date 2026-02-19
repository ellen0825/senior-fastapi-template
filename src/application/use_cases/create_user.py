from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository
from src.application.dto.user_dto import UserResponse


class CreateUserUseCase:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, email: str, name: str) -> UserResponse:
        user = User.create(email=email, name=name)
        self.repository.save(user)

        return UserResponse(
            id=user.id,
            email=user.email,
            name=user.name,
        )