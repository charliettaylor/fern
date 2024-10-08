"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.getErrorMessageForIncorrectType = void 0;
function getErrorMessageForIncorrectType(value, expectedType) {
    return `Expected ${expectedType}. Received ${getTypeAsString(value)}.`;
}
exports.getErrorMessageForIncorrectType = getErrorMessageForIncorrectType;
function getTypeAsString(value) {
    if (Array.isArray(value)) {
        return "list";
    }
    if (value === null) {
        return "null";
    }
    if (value instanceof BigInt) {
        return "BigInt";
    }
    switch (typeof value) {
        case "string":
            return `"${value}"`;
        case "bigint":
        case "number":
        case "boolean":
        case "undefined":
            return `${value}`;
    }
    return typeof value;
}
