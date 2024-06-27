/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as core from "../../../../core";
import * as SeedPagination from "../../../index";
import urlJoin from "url-join";
import * as serializers from "../../../../serialization/index";
import * as errors from "../../../../errors/index";

export declare namespace Users {
    interface Options {
        environment: core.Supplier<string>;
        token?: core.Supplier<core.BearerToken | undefined>;
    }

    interface RequestOptions {
        /** The maximum time to wait for a response in seconds. */
        timeoutInSeconds?: number;
        /** The number of times to retry the request. Defaults to 2. */
        maxRetries?: number;
        /** A hook to abort the request. */
        abortSignal?: AbortSignal;
    }
}

export class Users {
    constructor(protected readonly _options: Users.Options) {}

    /**
     * @param {SeedPagination.ListUsersCursorPaginationRequest} request
     * @param {Users.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.users.listWithCursorPagination({
     *         page: 1,
     *         perPage: 1,
     *         order: SeedPagination.Order.Asc,
     *         startingAfter: "string"
     *     })
     */
    public async listWithCursorPagination(
        request: SeedPagination.ListUsersCursorPaginationRequest = {},
        requestOptions?: Users.RequestOptions
    ): Promise<core.Page<SeedPagination.User>> {
        const list = async (
            request: SeedPagination.ListUsersCursorPaginationRequest
        ): Promise<SeedPagination.ListUsersPaginationResponse> => {
            const { page, perPage, order, startingAfter } = request;
            const _queryParams: Record<string, string | string[] | object | object[]> = {};
            if (page != null) {
                _queryParams["page"] = page.toString();
            }
            if (perPage != null) {
                _queryParams["per_page"] = perPage.toString();
            }
            if (order != null) {
                _queryParams["order"] = order;
            }
            if (startingAfter != null) {
                _queryParams["starting_after"] = startingAfter;
            }
            const _response = await core.fetcher({
                url: urlJoin(await core.Supplier.get(this._options.environment), "/users"),
                method: "GET",
                headers: {
                    Authorization: await this._getAuthorizationHeader(),
                    "X-Fern-Language": "JavaScript",
                    "X-Fern-SDK-Name": "@fern/pagination",
                    "X-Fern-SDK-Version": "0.0.1",
                    "X-Fern-Runtime": core.RUNTIME.type,
                    "X-Fern-Runtime-Version": core.RUNTIME.version,
                },
                contentType: "application/json",
                queryParameters: _queryParams,
                timeoutMs: requestOptions?.timeoutInSeconds != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
                maxRetries: requestOptions?.maxRetries,
                abortSignal: requestOptions?.abortSignal,
            });
            if (_response.ok) {
                return await serializers.ListUsersPaginationResponse.parseOrThrow(_response.body, {
                    unrecognizedObjectKeys: "passthrough",
                    allowUnrecognizedUnionMembers: true,
                    allowUnrecognizedEnumValues: true,
                    breadcrumbsPrefix: ["response"],
                });
            }
            if (_response.error.reason === "status-code") {
                throw new errors.SeedPaginationError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.body,
                });
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.SeedPaginationError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.SeedPaginationTimeoutError();
                case "unknown":
                    throw new errors.SeedPaginationError({
                        message: _response.error.errorMessage,
                    });
            }
        };
        return new core.Pageable<SeedPagination.ListUsersPaginationResponse, SeedPagination.User>({
            response: await list(request),
            hasNextPage: (response) => response?.page?.next?.startingAfter != null,
            getItems: (response) => response?.data ?? [],
            loadPage: (response) => {
                return list({
                    ...request,
                    startingAfter: response?.page?.next?.startingAfter,
                });
            },
        });
    }

    /**
     * @param {SeedPagination.ListUsersOffsetPaginationRequest} request
     * @param {Users.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.users.listWithOffsetPagination({
     *         page: 1,
     *         perPage: 1,
     *         order: SeedPagination.Order.Asc,
     *         startingAfter: "string"
     *     })
     */
    public async listWithOffsetPagination(
        request: SeedPagination.ListUsersOffsetPaginationRequest = {},
        requestOptions?: Users.RequestOptions
    ): Promise<SeedPagination.ListUsersPaginationResponse> {
        const { page, perPage, order, startingAfter } = request;
        const _queryParams: Record<string, string | string[] | object | object[]> = {};
        if (page != null) {
            _queryParams["page"] = page.toString();
        }

        if (perPage != null) {
            _queryParams["per_page"] = perPage.toString();
        }

        if (order != null) {
            _queryParams["order"] = order;
        }

        if (startingAfter != null) {
            _queryParams["starting_after"] = startingAfter;
        }

        const _response = await core.fetcher({
            url: urlJoin(await core.Supplier.get(this._options.environment), "/users"),
            method: "GET",
            headers: {
                Authorization: await this._getAuthorizationHeader(),
                "X-Fern-Language": "JavaScript",
                "X-Fern-SDK-Name": "@fern/pagination",
                "X-Fern-SDK-Version": "0.0.1",
                "X-Fern-Runtime": core.RUNTIME.type,
                "X-Fern-Runtime-Version": core.RUNTIME.version,
            },
            contentType: "application/json",
            queryParameters: _queryParams,
            timeoutMs: requestOptions?.timeoutInSeconds != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
            maxRetries: requestOptions?.maxRetries,
            abortSignal: requestOptions?.abortSignal,
        });
        if (_response.ok) {
            return await serializers.ListUsersPaginationResponse.parseOrThrow(_response.body, {
                unrecognizedObjectKeys: "passthrough",
                allowUnrecognizedUnionMembers: true,
                allowUnrecognizedEnumValues: true,
                breadcrumbsPrefix: ["response"],
            });
        }

        if (_response.error.reason === "status-code") {
            throw new errors.SeedPaginationError({
                statusCode: _response.error.statusCode,
                body: _response.error.body,
            });
        }

        switch (_response.error.reason) {
            case "non-json":
                throw new errors.SeedPaginationError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.rawBody,
                });
            case "timeout":
                throw new errors.SeedPaginationTimeoutError();
            case "unknown":
                throw new errors.SeedPaginationError({
                    message: _response.error.errorMessage,
                });
        }
    }

    /**
     * @param {SeedPagination.ListUsersOffsetStepPaginationRequest} request
     * @param {Users.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.users.listWithOffsetStepPagination({
     *         page: 1,
     *         limit: 1,
     *         order: SeedPagination.Order.Asc
     *     })
     */
    public async listWithOffsetStepPagination(
        request: SeedPagination.ListUsersOffsetStepPaginationRequest = {},
        requestOptions?: Users.RequestOptions
    ): Promise<SeedPagination.ListUsersPaginationResponse> {
        const { page, limit, order } = request;
        const _queryParams: Record<string, string | string[] | object | object[]> = {};
        if (page != null) {
            _queryParams["page"] = page.toString();
        }

        if (limit != null) {
            _queryParams["limit"] = limit.toString();
        }

        if (order != null) {
            _queryParams["order"] = order;
        }

        const _response = await core.fetcher({
            url: urlJoin(await core.Supplier.get(this._options.environment), "/users"),
            method: "GET",
            headers: {
                Authorization: await this._getAuthorizationHeader(),
                "X-Fern-Language": "JavaScript",
                "X-Fern-SDK-Name": "@fern/pagination",
                "X-Fern-SDK-Version": "0.0.1",
                "X-Fern-Runtime": core.RUNTIME.type,
                "X-Fern-Runtime-Version": core.RUNTIME.version,
            },
            contentType: "application/json",
            queryParameters: _queryParams,
            timeoutMs: requestOptions?.timeoutInSeconds != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
            maxRetries: requestOptions?.maxRetries,
            abortSignal: requestOptions?.abortSignal,
        });
        if (_response.ok) {
            return await serializers.ListUsersPaginationResponse.parseOrThrow(_response.body, {
                unrecognizedObjectKeys: "passthrough",
                allowUnrecognizedUnionMembers: true,
                allowUnrecognizedEnumValues: true,
                breadcrumbsPrefix: ["response"],
            });
        }

        if (_response.error.reason === "status-code") {
            throw new errors.SeedPaginationError({
                statusCode: _response.error.statusCode,
                body: _response.error.body,
            });
        }

        switch (_response.error.reason) {
            case "non-json":
                throw new errors.SeedPaginationError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.rawBody,
                });
            case "timeout":
                throw new errors.SeedPaginationTimeoutError();
            case "unknown":
                throw new errors.SeedPaginationError({
                    message: _response.error.errorMessage,
                });
        }
    }

    /**
     * @param {SeedPagination.ListUsersExtendedRequest} request
     * @param {Users.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.users.listWithExtendedResults({
     *         cursor: "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32"
     *     })
     */
    public async listWithExtendedResults(
        request: SeedPagination.ListUsersExtendedRequest = {},
        requestOptions?: Users.RequestOptions
    ): Promise<core.Page<SeedPagination.User>> {
        const list = async (
            request: SeedPagination.ListUsersExtendedRequest
        ): Promise<SeedPagination.ListUsersExtendedResponse> => {
            const { cursor } = request;
            const _queryParams: Record<string, string | string[] | object | object[]> = {};
            if (cursor != null) {
                _queryParams["cursor"] = cursor;
            }
            const _response = await core.fetcher({
                url: urlJoin(await core.Supplier.get(this._options.environment), "/users"),
                method: "GET",
                headers: {
                    Authorization: await this._getAuthorizationHeader(),
                    "X-Fern-Language": "JavaScript",
                    "X-Fern-SDK-Name": "@fern/pagination",
                    "X-Fern-SDK-Version": "0.0.1",
                    "X-Fern-Runtime": core.RUNTIME.type,
                    "X-Fern-Runtime-Version": core.RUNTIME.version,
                },
                contentType: "application/json",
                queryParameters: _queryParams,
                timeoutMs: requestOptions?.timeoutInSeconds != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
                maxRetries: requestOptions?.maxRetries,
                abortSignal: requestOptions?.abortSignal,
            });
            if (_response.ok) {
                return await serializers.ListUsersExtendedResponse.parseOrThrow(_response.body, {
                    unrecognizedObjectKeys: "passthrough",
                    allowUnrecognizedUnionMembers: true,
                    allowUnrecognizedEnumValues: true,
                    breadcrumbsPrefix: ["response"],
                });
            }
            if (_response.error.reason === "status-code") {
                throw new errors.SeedPaginationError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.body,
                });
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.SeedPaginationError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.SeedPaginationTimeoutError();
                case "unknown":
                    throw new errors.SeedPaginationError({
                        message: _response.error.errorMessage,
                    });
            }
        };
        return new core.Pageable<SeedPagination.ListUsersExtendedResponse, SeedPagination.User>({
            response: await list(request),
            hasNextPage: (response) => response?.next != null,
            getItems: (response) => response?.data?.users ?? [],
            loadPage: (response) => {
                return list({
                    ...request,
                    cursor: response?.next,
                });
            },
        });
    }

    /**
     * @param {SeedPagination.ListUsernamesRequest} request
     * @param {Users.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.users.listUsernames({
     *         startingAfter: "string"
     *     })
     */
    public async listUsernames(
        request: SeedPagination.ListUsernamesRequest = {},
        requestOptions?: Users.RequestOptions
    ): Promise<core.Page<string>> {
        const list = async (request: SeedPagination.ListUsernamesRequest): Promise<SeedPagination.UsernameCursor> => {
            const { startingAfter } = request;
            const _queryParams: Record<string, string | string[] | object | object[]> = {};
            if (startingAfter != null) {
                _queryParams["starting_after"] = startingAfter;
            }
            const _response = await core.fetcher({
                url: urlJoin(await core.Supplier.get(this._options.environment), "/users"),
                method: "GET",
                headers: {
                    Authorization: await this._getAuthorizationHeader(),
                    "X-Fern-Language": "JavaScript",
                    "X-Fern-SDK-Name": "@fern/pagination",
                    "X-Fern-SDK-Version": "0.0.1",
                    "X-Fern-Runtime": core.RUNTIME.type,
                    "X-Fern-Runtime-Version": core.RUNTIME.version,
                },
                contentType: "application/json",
                queryParameters: _queryParams,
                timeoutMs: requestOptions?.timeoutInSeconds != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
                maxRetries: requestOptions?.maxRetries,
                abortSignal: requestOptions?.abortSignal,
            });
            if (_response.ok) {
                return await serializers.UsernameCursor.parseOrThrow(_response.body, {
                    unrecognizedObjectKeys: "passthrough",
                    allowUnrecognizedUnionMembers: true,
                    allowUnrecognizedEnumValues: true,
                    breadcrumbsPrefix: ["response"],
                });
            }
            if (_response.error.reason === "status-code") {
                throw new errors.SeedPaginationError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.body,
                });
            }
            switch (_response.error.reason) {
                case "non-json":
                    throw new errors.SeedPaginationError({
                        statusCode: _response.error.statusCode,
                        body: _response.error.rawBody,
                    });
                case "timeout":
                    throw new errors.SeedPaginationTimeoutError();
                case "unknown":
                    throw new errors.SeedPaginationError({
                        message: _response.error.errorMessage,
                    });
            }
        };
        return new core.Pageable<SeedPagination.UsernameCursor, string>({
            response: await list(request),
            hasNextPage: (response) => response?.cursor?.after != null,
            getItems: (response) => response?.cursor?.data ?? [],
            loadPage: (response) => {
                return list({
                    ...request,
                    startingAfter: response?.cursor?.after,
                });
            },
        });
    }

    /**
     * @param {SeedPagination.ListWithGlobalConfigRequest} request
     * @param {Users.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.users.listWithGlobalConfig({
     *         offset: 1
     *     })
     */
    public async listWithGlobalConfig(
        request: SeedPagination.ListWithGlobalConfigRequest = {},
        requestOptions?: Users.RequestOptions
    ): Promise<SeedPagination.UsernameContainer> {
        const { offset } = request;
        const _queryParams: Record<string, string | string[] | object | object[]> = {};
        if (offset != null) {
            _queryParams["offset"] = offset.toString();
        }

        const _response = await core.fetcher({
            url: urlJoin(await core.Supplier.get(this._options.environment), "/users"),
            method: "GET",
            headers: {
                Authorization: await this._getAuthorizationHeader(),
                "X-Fern-Language": "JavaScript",
                "X-Fern-SDK-Name": "@fern/pagination",
                "X-Fern-SDK-Version": "0.0.1",
                "X-Fern-Runtime": core.RUNTIME.type,
                "X-Fern-Runtime-Version": core.RUNTIME.version,
            },
            contentType: "application/json",
            queryParameters: _queryParams,
            timeoutMs: requestOptions?.timeoutInSeconds != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
            maxRetries: requestOptions?.maxRetries,
            abortSignal: requestOptions?.abortSignal,
        });
        if (_response.ok) {
            return await serializers.UsernameContainer.parseOrThrow(_response.body, {
                unrecognizedObjectKeys: "passthrough",
                allowUnrecognizedUnionMembers: true,
                allowUnrecognizedEnumValues: true,
                breadcrumbsPrefix: ["response"],
            });
        }

        if (_response.error.reason === "status-code") {
            throw new errors.SeedPaginationError({
                statusCode: _response.error.statusCode,
                body: _response.error.body,
            });
        }

        switch (_response.error.reason) {
            case "non-json":
                throw new errors.SeedPaginationError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.rawBody,
                });
            case "timeout":
                throw new errors.SeedPaginationTimeoutError();
            case "unknown":
                throw new errors.SeedPaginationError({
                    message: _response.error.errorMessage,
                });
        }
    }

    protected async _getAuthorizationHeader(): Promise<string | undefined> {
        const bearer = await core.Supplier.get(this._options.token);
        if (bearer != null) {
            return `Bearer ${bearer}`;
        }

        return undefined;
    }
}
