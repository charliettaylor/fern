/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as core from "../../../../core";
import * as SeedMixedCase from "../../../index";
import urlJoin from "url-join";
import * as serializers from "../../../../serialization/index";
import * as errors from "../../../../errors/index";

export declare namespace Service {
    interface Options {
        environment: core.Supplier<string>;
    }

    interface RequestOptions {
        timeoutInSeconds?: number;
        maxRetries?: number;
        abortSignal?: AbortSignal;
    }
}

export class Service {
    constructor(protected readonly _options: Service.Options) {}

    /**
     * @param {string} resourceId
     * @param {Service.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.service.getResource("rsc-xyz")
     */
    public async getResource(
        resourceId: string,
        requestOptions?: Service.RequestOptions
    ): Promise<SeedMixedCase.Resource> {
        const _response = await core.fetcher({
            url: urlJoin(
                await core.Supplier.get(this._options.environment),
                `/resource/${encodeURIComponent(resourceId)}`
            ),
            method: "GET",
            headers: {
                "X-Fern-Language": "JavaScript",
                "X-Fern-SDK-Name": "@fern/mixed-case",
                "X-Fern-SDK-Version": "0.0.1",
                "X-Fern-Runtime": core.RUNTIME.type,
                "X-Fern-Runtime-Version": core.RUNTIME.version,
            },
            contentType: "application/json",
            timeoutMs: requestOptions?.timeoutInSeconds != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
            maxRetries: requestOptions?.maxRetries,
            abortSignal: requestOptions?.abortSignal,
        });
        if (_response.ok) {
            return await serializers.Resource.parseOrThrow(_response.body, {
                unrecognizedObjectKeys: "passthrough",
                allowUnrecognizedUnionMembers: true,
                allowUnrecognizedEnumValues: true,
                breadcrumbsPrefix: ["response"],
            });
        }

        if (_response.error.reason === "status-code") {
            throw new errors.SeedMixedCaseError({
                statusCode: _response.error.statusCode,
                body: _response.error.body,
            });
        }

        switch (_response.error.reason) {
            case "non-json":
                throw new errors.SeedMixedCaseError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.rawBody,
                });
            case "timeout":
                throw new errors.SeedMixedCaseTimeoutError();
            case "unknown":
                throw new errors.SeedMixedCaseError({
                    message: _response.error.errorMessage,
                });
        }
    }

    /**
     * @param {SeedMixedCase.ListResourcesRequest} request
     * @param {Service.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.service.listResources({
     *         pageLimit: 10,
     *         beforeDate: "2023-01-01"
     *     })
     */
    public async listResources(
        request: SeedMixedCase.ListResourcesRequest,
        requestOptions?: Service.RequestOptions
    ): Promise<SeedMixedCase.Resource[]> {
        const { pageLimit, beforeDate } = request;
        const _queryParams: Record<string, string | string[] | object | object[]> = {};
        _queryParams["page_limit"] = pageLimit.toString();
        _queryParams["beforeDate"] = beforeDate;
        const _response = await core.fetcher({
            url: urlJoin(await core.Supplier.get(this._options.environment), "/resource"),
            method: "GET",
            headers: {
                "X-Fern-Language": "JavaScript",
                "X-Fern-SDK-Name": "@fern/mixed-case",
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
            return await serializers.service.listResources.Response.parseOrThrow(_response.body, {
                unrecognizedObjectKeys: "passthrough",
                allowUnrecognizedUnionMembers: true,
                allowUnrecognizedEnumValues: true,
                breadcrumbsPrefix: ["response"],
            });
        }

        if (_response.error.reason === "status-code") {
            throw new errors.SeedMixedCaseError({
                statusCode: _response.error.statusCode,
                body: _response.error.body,
            });
        }

        switch (_response.error.reason) {
            case "non-json":
                throw new errors.SeedMixedCaseError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.rawBody,
                });
            case "timeout":
                throw new errors.SeedMixedCaseTimeoutError();
            case "unknown":
                throw new errors.SeedMixedCaseError({
                    message: _response.error.errorMessage,
                });
        }
    }
}
