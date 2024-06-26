/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "../../..";
import * as SeedTrace from "../../../../api";
import * as core from "../../../../core";
export declare const RecordedTestCaseUpdate: core.serialization.ObjectSchema<serializers.RecordedTestCaseUpdate.Raw, SeedTrace.RecordedTestCaseUpdate>;
export declare namespace RecordedTestCaseUpdate {
    interface Raw {
        testCaseId: serializers.v2.TestCaseId.Raw;
        traceResponsesSize: number;
    }
}
