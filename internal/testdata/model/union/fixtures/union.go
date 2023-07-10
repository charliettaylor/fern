// This file was auto-generated by Fern from our API Definition.

package api

import (
	json "encoding/json"
	fmt "fmt"
)

// This is a simple union.
type Union struct {
	Type string
	Foo  *Foo
	Bar  *Bar
}

func NewUnionFromFoo(value *Foo) *Union {
	return &Union{Type: "foo", Foo: value}
}

func NewUnionFromBar(value *Bar) *Union {
	return &Union{Type: "bar", Bar: value}
}

func (u *Union) UnmarshalJSON(data []byte) error {
	var unmarshaler struct {
		Type string `json:"type"`
	}
	if err := json.Unmarshal(data, &unmarshaler); err != nil {
		return err
	}
	u.Type = unmarshaler.Type
	switch unmarshaler.Type {
	case "foo":
		var valueUnmarshaler struct {
			Foo *Foo `json:"foo,omitempty"`
		}
		if err := json.Unmarshal(data, &valueUnmarshaler); err != nil {
			return err
		}
		u.Foo = valueUnmarshaler.Foo
	case "bar":
		var valueUnmarshaler struct {
			Bar *Bar `json:"bar,omitempty"`
		}
		if err := json.Unmarshal(data, &valueUnmarshaler); err != nil {
			return err
		}
		u.Bar = valueUnmarshaler.Bar
	}
	return nil
}

func (u Union) MarshalJSON() ([]byte, error) {
	switch u.Type {
	default:
		return nil, fmt.Errorf("invalid type %s in %T", u.Type, u)
	case "foo":
		var marshaler = struct {
			Type string `json:"type"`
			Foo  *Foo   `json:"foo,omitempty"`
		}{
			Type: u.Type,
			Foo:  u.Foo,
		}
		return json.Marshal(marshaler)
	case "bar":
		var marshaler = struct {
			Type string `json:"type"`
			Bar  *Bar   `json:"bar,omitempty"`
		}{
			Type: u.Type,
			Bar:  u.Bar,
		}
		return json.Marshal(marshaler)
	}
}

type UnionVisitor interface {
	VisitFoo(*Foo) error
	VisitBar(*Bar) error
}

func (u *Union) Accept(v UnionVisitor) error {
	switch u.Type {
	default:
		return fmt.Errorf("invalid type %s in %T", u.Type, u)
	case "foo":
		return v.VisitFoo(u.Foo)
	case "bar":
		return v.VisitBar(u.Bar)
	}
}
