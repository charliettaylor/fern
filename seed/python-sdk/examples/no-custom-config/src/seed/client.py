# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

import httpx

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.jsonable_encoder import jsonable_encoder
from .core.pydantic_utilities import pydantic_v1
from .core.query_encoder import encode_query
from .core.remove_none_from_dict import remove_none_from_dict
from .core.request_options import RequestOptions
from .environment import SeedExamplesEnvironment
from .file.client import AsyncFileClient, FileClient
from .health.client import AsyncHealthClient, HealthClient
from .service.client import AsyncServiceClient, ServiceClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SeedExamples:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : typing.Optional[SeedExamplesEnvironment]
        The environment to use for requests from the client.

    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from seed.client import SeedExamples
    from seed.environment import SeedExamplesEnvironment

    client = SeedExamples(
        token="YOUR_TOKEN",
        environment=SeedExamplesEnvironment.PRODUCTION,
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: typing.Optional[SeedExamplesEnvironment] = None,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.file = FileClient(client_wrapper=self._client_wrapper)
        self.health = HealthClient(client_wrapper=self._client_wrapper)
        self.service = ServiceClient(client_wrapper=self._client_wrapper)

    def echo(self, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str

        Examples
        --------
        from seed.client import SeedExamples
        from seed.environment import SeedExamplesEnvironment

        client = SeedExamples(
            token="YOUR_TOKEN",
            environment=SeedExamplesEnvironment.PRODUCTION,
        )
        client.echo(
            request="Hello world!\\n\\nwith\\n\\tnewlines",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=self._client_wrapper.get_base_url(),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(request),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(str, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncSeedExamples:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : typing.Optional[SeedExamplesEnvironment]
        The environment to use for requests from the client.

    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from seed.client import AsyncSeedExamples
    from seed.environment import SeedExamplesEnvironment

    client = AsyncSeedExamples(
        token="YOUR_TOKEN",
        environment=SeedExamplesEnvironment.PRODUCTION,
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: typing.Optional[SeedExamplesEnvironment] = None,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.file = AsyncFileClient(client_wrapper=self._client_wrapper)
        self.health = AsyncHealthClient(client_wrapper=self._client_wrapper)
        self.service = AsyncServiceClient(client_wrapper=self._client_wrapper)

    async def echo(self, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str

        Examples
        --------
        from seed.client import AsyncSeedExamples
        from seed.environment import SeedExamplesEnvironment

        client = AsyncSeedExamples(
            token="YOUR_TOKEN",
            environment=SeedExamplesEnvironment.PRODUCTION,
        )
        await client.echo(
            request="Hello world!\\n\\nwith\\n\\tnewlines",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=self._client_wrapper.get_base_url(),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(request),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(str, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


def _get_base_url(
    *, base_url: typing.Optional[str] = None, environment: typing.Optional[SeedExamplesEnvironment] = None
) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
