# This file was auto-generated by Fern from our API Definition.

from ...core.api_error import ApiError
from .animal import Animal


class ErrorWithUnionBody(ApiError):
    def __init__(self, body: Animal):
        super().__init__(status_code=400, body=body)
