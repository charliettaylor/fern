# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .custom_auth._client import AsyncCustomAuthClient, CustomAuthClient


class SeedCustomAuth:
    def __init__(
        self,
        *,
        base_url: str,
        custom_auth_scheme: str,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=base_url,
            custom_auth_scheme=custom_auth_scheme,
            httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.custom_auth = CustomAuthClient(client_wrapper=self._client_wrapper)


class AsyncSeedCustomAuth:
    def __init__(
        self,
        *,
        base_url: str,
        custom_auth_scheme: str,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=base_url,
            custom_auth_scheme=custom_auth_scheme,
            httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.custom_auth = AsyncCustomAuthClient(client_wrapper=self._client_wrapper)
