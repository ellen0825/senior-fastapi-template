class DomainError(Exception):
    pass


class UserAlreadyExistsError(DomainError):
    pass