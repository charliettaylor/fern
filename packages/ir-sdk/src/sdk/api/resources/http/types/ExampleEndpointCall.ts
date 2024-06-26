/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as FernIr from "../../..";

export interface ExampleEndpointCall extends FernIr.WithDocs {
    name: FernIr.Name | undefined;
    url: string;
    rootPathParameters: FernIr.ExamplePathParameter[];
    servicePathParameters: FernIr.ExamplePathParameter[];
    endpointPathParameters: FernIr.ExamplePathParameter[];
    serviceHeaders: FernIr.ExampleHeader[];
    endpointHeaders: FernIr.ExampleHeader[];
    queryParameters: FernIr.ExampleQueryParameter[];
    request: FernIr.ExampleRequestBody | undefined;
    response: FernIr.ExampleResponse;
    /**
     * Hand-written code samples for this endpoint. These code samples should match the
     * example that it's attached to, so that we can spin up an API Playground with
     * the code sample that's being displayed in the API Reference.
     */
    codeSamples: FernIr.ExampleCodeSample[] | undefined;
}
