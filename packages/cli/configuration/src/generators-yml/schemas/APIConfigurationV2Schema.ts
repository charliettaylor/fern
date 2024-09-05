import { z } from "zod";
import { RawSchemas } from "@fern-api/fern-definition-schema";

export const OpenAPISpecSchema = z.strictObject({
    openapi: z.string(),
    overrides: z.string().optional(),
    namespace: z.string().optional()
});

export type OpenAPISpecSchema = z.infer<typeof OpenAPISpecSchema>;

export const AsyncAPISchema = z.strictObject({
    asyncapi: z.string(),
    overrides: z.string().optional(),
    namespace: z.string().optional()
});

export type AsyncAPISchema = z.infer<typeof AsyncAPISchema>;

export const SpecSchema = z.union([OpenAPISpecSchema, AsyncAPISchema]);

export type SpecSchema = z.infer<typeof SpecSchema>;

export const APIConfigurationV2Schema = RawSchemas.WithEnvironmentsSchema.extend({
    auth: z.optional(RawSchemas.ApiAuthSchema),
    specs: z.array(SpecSchema)
});
