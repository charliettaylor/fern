/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "../../..";
import * as SeedCustomAuth from "../../../../api";
import * as core from "../../../../core";
export declare const UnauthorizedRequestErrorBody: core.serialization.ObjectSchema<serializers.UnauthorizedRequestErrorBody.Raw, SeedCustomAuth.UnauthorizedRequestErrorBody>;
export declare namespace UnauthorizedRequestErrorBody {
    interface Raw {
        message: string;
    }
}
