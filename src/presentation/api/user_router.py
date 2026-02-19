from fastapi import APIRouter, Depends
from src.application.use_cases.create_user import CreateUserUseCase
from src.infrastructure.repositories.user_repository_impl import InMemoryUserRepository
from src.application.dto.user_dto import CreateUserRequest, UserResponse

router = APIRouter()
repository = InMemoryUserRepository()


def get_use_case():
    return CreateUserUseCase(repository)


@router.post("/users", response_model=UserResponse)
def create_user(
    request: CreateUserRequest,
    use_case: CreateUserUseCase = Depends(get_use_case),
):
    return use_case.execute(request.email, request.name)