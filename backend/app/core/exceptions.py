class APIException(Exception):
    status_code = 400

    def __init__(self, message: str, detail: dict | None = None):
        self.message = message
        self.detail = detail
        super().__init__(message)


class BadRequestException(APIException):
    status_code = 400


class UnauthorizedException(APIException):
    status_code = 401


class ForbiddenException(APIException):
    status_code = 403


class NotFoundException(APIException):
    status_code = 404


class ConflictException(APIException):
    status_code = 409


class InternalServerException(APIException):
    status_code = 500
