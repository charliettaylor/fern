/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as core from "../../../../core";
import * as SeedOauthClientCredentialsEnvironmentVariables from "../../../index";
import * as serializers from "../../../../serialization/index";
import urlJoin from "url-join";
import * as errors from "../../../../errors/index";

export declare namespace Auth {
    interface Options {
        environment: core.Supplier<string>;
        token?: core.Supplier<core.BearerToken | undefined>;
    }

    interface RequestOptions {
        timeoutInSeconds?: number;
        maxRetries?: number;
        abortSignal?: AbortSignal;
    }
}

export class Auth {
    constructor(protected readonly _options: Auth.Options) {}

    /**
     * @param {SeedOauthClientCredentialsEnvironmentVariables.GetTokenRequest} request
     * @param {Auth.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.auth.getTokenWithClientCredentials({
     *         clientId: "string",
     *         clientSecret: "string",
     *         audience: "https://api.example.com",
     *         grantType: "client_credentials",
     *         scope: "string"
     *     })
     */
    public async getTokenWithClientCredentials(
        request: SeedOauthClientCredentialsEnvironmentVariables.GetTokenRequest,
        requestOptions?: Auth.RequestOptions
    ): Promise<SeedOauthClientCredentialsEnvironmentVariables.TokenResponse> {
        const _response = await core.fetcher({
            url: urlJoin(await core.Supplier.get(this._options.environment), "/token"),
            method: "POST",
            headers: {
                Authorization: await this._getAuthorizationHeader(),
                "X-Fern-Language": "JavaScript",
                "X-Fern-SDK-Name": "@fern/oauth-client-credentials-environment-variables",
                "X-Fern-SDK-Version": "0.0.1",
                "X-Fern-Runtime": core.RUNTIME.type,
                "X-Fern-Runtime-Version": core.RUNTIME.version,
            },
            contentType: "application/json",
            body: {
                ...(await serializers.GetTokenRequest.jsonOrThrow(request, { unrecognizedObjectKeys: "strip" })),
                audience: "https://api.example.com",
                grant_type: "client_credentials",
            },
            timeoutMs: requestOptions?.timeoutInSeconds != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
            maxRetries: requestOptions?.maxRetries,
            abortSignal: requestOptions?.abortSignal,
        });
        if (_response.ok) {
            return await serializers.TokenResponse.parseOrThrow(_response.body, {
                unrecognizedObjectKeys: "passthrough",
                allowUnrecognizedUnionMembers: true,
                allowUnrecognizedEnumValues: true,
                breadcrumbsPrefix: ["response"],
            });
        }

        if (_response.error.reason === "status-code") {
            throw new errors.SeedOauthClientCredentialsEnvironmentVariablesError({
                statusCode: _response.error.statusCode,
                body: _response.error.body,
            });
        }

        switch (_response.error.reason) {
            case "non-json":
                throw new errors.SeedOauthClientCredentialsEnvironmentVariablesError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.rawBody,
                });
            case "timeout":
                throw new errors.SeedOauthClientCredentialsEnvironmentVariablesTimeoutError();
            case "unknown":
                throw new errors.SeedOauthClientCredentialsEnvironmentVariablesError({
                    message: _response.error.errorMessage,
                });
        }
    }

    /**
     * @param {SeedOauthClientCredentialsEnvironmentVariables.RefreshTokenRequest} request
     * @param {Auth.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @example
     *     await client.auth.refreshToken({
     *         clientId: "string",
     *         clientSecret: "string",
     *         refreshToken: "string",
     *         audience: "https://api.example.com",
     *         grantType: "refresh_token",
     *         scope: "string"
     *     })
     */
    public async refreshToken(
        request: SeedOauthClientCredentialsEnvironmentVariables.RefreshTokenRequest,
        requestOptions?: Auth.RequestOptions
    ): Promise<SeedOauthClientCredentialsEnvironmentVariables.TokenResponse> {
        const _response = await core.fetcher({
            url: urlJoin(await core.Supplier.get(this._options.environment), "/token"),
            method: "POST",
            headers: {
                Authorization: await this._getAuthorizationHeader(),
                "X-Fern-Language": "JavaScript",
                "X-Fern-SDK-Name": "@fern/oauth-client-credentials-environment-variables",
                "X-Fern-SDK-Version": "0.0.1",
                "X-Fern-Runtime": core.RUNTIME.type,
                "X-Fern-Runtime-Version": core.RUNTIME.version,
            },
            contentType: "application/json",
            body: {
                ...(await serializers.RefreshTokenRequest.jsonOrThrow(request, { unrecognizedObjectKeys: "strip" })),
                audience: "https://api.example.com",
                grant_type: "refresh_token",
            },
            timeoutMs: requestOptions?.timeoutInSeconds != null ? requestOptions.timeoutInSeconds * 1000 : 60000,
            maxRetries: requestOptions?.maxRetries,
            abortSignal: requestOptions?.abortSignal,
        });
        if (_response.ok) {
            return await serializers.TokenResponse.parseOrThrow(_response.body, {
                unrecognizedObjectKeys: "passthrough",
                allowUnrecognizedUnionMembers: true,
                allowUnrecognizedEnumValues: true,
                breadcrumbsPrefix: ["response"],
            });
        }

        if (_response.error.reason === "status-code") {
            throw new errors.SeedOauthClientCredentialsEnvironmentVariablesError({
                statusCode: _response.error.statusCode,
                body: _response.error.body,
            });
        }

        switch (_response.error.reason) {
            case "non-json":
                throw new errors.SeedOauthClientCredentialsEnvironmentVariablesError({
                    statusCode: _response.error.statusCode,
                    body: _response.error.rawBody,
                });
            case "timeout":
                throw new errors.SeedOauthClientCredentialsEnvironmentVariablesTimeoutError();
            case "unknown":
                throw new errors.SeedOauthClientCredentialsEnvironmentVariablesError({
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
