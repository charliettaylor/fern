/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "..";
import * as SeedApi from "../../api";
import * as core from "../../core";
export declare const ImportingA: core.serialization.ObjectSchema<serializers.ImportingA.Raw, SeedApi.ImportingA>;
export declare namespace ImportingA {
    interface Raw {
        a?: serializers.A.Raw | null;
    }
}
