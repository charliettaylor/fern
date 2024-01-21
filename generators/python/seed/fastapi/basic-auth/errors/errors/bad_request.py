# This file was auto-generated by Fern from our API Definition.

from ...core.exceptions.fern_http_exception import FernHTTPException


class BadRequest(FernHTTPException):
    def __init__(self) -> None:
        super().__init__(status_code=400, name="BadRequest")
