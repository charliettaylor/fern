# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .endpoints._client import AsyncEndpointsClient, EndpointsClient
from .inlined_requests._client import AsyncInlinedRequestsClient, InlinedRequestsClient
from .no_auth._client import AsyncNoAuthClient, NoAuthClient
from .no_req_body._client import AsyncNoReqBodyClient, NoReqBodyClient
from .req_with_headers._client import AsyncReqWithHeadersClient, ReqWithHeadersClient


class SeedExhaustive:
    def __init__(
        self,
        *,
        base_url: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = 5,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=base_url,
            token=token,
            httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.endpoints = EndpointsClient(client_wrapper=self._client_wrapper)
        self.inlined_requests = InlinedRequestsClient(client_wrapper=self._client_wrapper)
        self.no_auth = NoAuthClient(client_wrapper=self._client_wrapper)
        self.no_req_body = NoReqBodyClient(client_wrapper=self._client_wrapper)
        self.req_with_headers = ReqWithHeadersClient(client_wrapper=self._client_wrapper)


class AsyncSeedExhaustive:
    def __init__(
        self,
        *,
        base_url: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = 5,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=base_url,
            token=token,
            httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.endpoints = AsyncEndpointsClient(client_wrapper=self._client_wrapper)
        self.inlined_requests = AsyncInlinedRequestsClient(client_wrapper=self._client_wrapper)
        self.no_auth = AsyncNoAuthClient(client_wrapper=self._client_wrapper)
        self.no_req_body = AsyncNoReqBodyClient(client_wrapper=self._client_wrapper)
        self.req_with_headers = AsyncReqWithHeadersClient(client_wrapper=self._client_wrapper)
