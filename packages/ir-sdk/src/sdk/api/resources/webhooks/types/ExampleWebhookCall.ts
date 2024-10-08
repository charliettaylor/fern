/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernIr from "../../../index";

/**
 * An example webhook call. For now, this only includes the payload,
 * but it can be easily extended to support other endpoint properties
 * (e.g. headers).
 */
export interface ExampleWebhookCall extends FernIr.WithDocs {
    name: FernIr.Name | undefined;
    payload: FernIr.ExampleTypeReference;
}
