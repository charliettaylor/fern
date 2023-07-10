// This file was auto-generated by Fern from our API Definition.

package api

import (
	json "encoding/json"
	fmt "fmt"
)

type UnionWithPrimitive struct {
	Type    string
	Boolean bool
	String  string
}

func NewUnionWithPrimitiveFromBoolean(value bool) *UnionWithPrimitive {
	return &UnionWithPrimitive{Type: "boolean", Boolean: value}
}

func NewUnionWithPrimitiveFromString(value string) *UnionWithPrimitive {
	return &UnionWithPrimitive{Type: "string", String: value}
}

func (u *UnionWithPrimitive) UnmarshalJSON(data []byte) error {
	var unmarshaler struct {
		Type string `json:"type"`
	}
	if err := json.Unmarshal(data, &unmarshaler); err != nil {
		return err
	}
	u.Type = unmarshaler.Type
	switch unmarshaler.Type {
	case "boolean":
		var valueUnmarshaler struct {
			Boolean bool `json:"value"`
		}
		if err := json.Unmarshal(data, &valueUnmarshaler); err != nil {
			return err
		}
		u.Boolean = valueUnmarshaler.Boolean
	case "string":
		var valueUnmarshaler struct {
			String string `json:"value"`
		}
		if err := json.Unmarshal(data, &valueUnmarshaler); err != nil {
			return err
		}
		u.String = valueUnmarshaler.String
	}
	return nil
}

func (u UnionWithPrimitive) MarshalJSON() ([]byte, error) {
	switch u.Type {
	default:
		return nil, fmt.Errorf("invalid type %s in %T", u.Type, u)
	case "boolean":
		var marshaler = struct {
			Type    string `json:"type"`
			Boolean bool   `json:"value"`
		}{
			Type:    u.Type,
			Boolean: u.Boolean,
		}
		return json.Marshal(marshaler)
	case "string":
		var marshaler = struct {
			Type   string `json:"type"`
			String string `json:"value"`
		}{
			Type:   u.Type,
			String: u.String,
		}
		return json.Marshal(marshaler)
	}
}

type UnionWithPrimitiveVisitor interface {
	VisitBoolean(bool) error
	VisitString(string) error
}

func (u *UnionWithPrimitive) Accept(v UnionWithPrimitiveVisitor) error {
	switch u.Type {
	default:
		return fmt.Errorf("invalid type %s in %T", u.Type, u)
	case "boolean":
		return v.VisitBoolean(u.Boolean)
	case "string":
		return v.VisitString(u.String)
	}
}
