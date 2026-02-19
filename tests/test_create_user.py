from src.application.use_cases.create_user import CreateUserUseCase
from src.infrastructure.repositories.user_repository_impl import InMemoryUserRepository


def test_create_user():
    repo = InMemoryUserRepository()
    use_case = CreateUserUseCase(repo)

    result = use_case.execute("test@example.com", "Jerry")

    assert result.email == "test@example.com"
    assert result.name == "Jerry"