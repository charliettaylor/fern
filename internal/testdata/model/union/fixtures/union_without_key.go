// This file was auto-generated by Fern from our API Definition.

package api

import (
	json "encoding/json"
	fmt "fmt"
)

type UnionWithoutKey struct {
	Type string
	Foo  *Foo
	// This is a bar field.
	Bar *Bar
}

func NewUnionWithoutKeyFromFoo(value *Foo) *UnionWithoutKey {
	return &UnionWithoutKey{Type: "foo", Foo: value}
}

func NewUnionWithoutKeyFromBar(value *Bar) *UnionWithoutKey {
	return &UnionWithoutKey{Type: "bar", Bar: value}
}

func (u *UnionWithoutKey) UnmarshalJSON(data []byte) error {
	var unmarshaler struct {
		Type string `json:"type"`
	}
	if err := json.Unmarshal(data, &unmarshaler); err != nil {
		return err
	}
	u.Type = unmarshaler.Type
	switch unmarshaler.Type {
	case "foo":
		value := new(Foo)
		if err := json.Unmarshal(data, &value); err != nil {
			return err
		}
		u.Foo = value
	case "bar":
		value := new(Bar)
		if err := json.Unmarshal(data, &value); err != nil {
			return err
		}
		u.Bar = value
	}
	return nil
}

func (u UnionWithoutKey) MarshalJSON() ([]byte, error) {
	switch u.Type {
	default:
		return nil, fmt.Errorf("invalid type %s in %T", u.Type, u)
	case "foo":
		var marshaler = struct {
			Type string `json:"type"`
			*Foo
		}{
			Type: u.Type,
			Foo:  u.Foo,
		}
		return json.Marshal(marshaler)
	case "bar":
		var marshaler = struct {
			Type string `json:"type"`
			*Bar
		}{
			Type: u.Type,
			Bar:  u.Bar,
		}
		return json.Marshal(marshaler)
	}
}

type UnionWithoutKeyVisitor interface {
	VisitFoo(*Foo) error
	VisitBar(*Bar) error
}

func (u *UnionWithoutKey) Accept(v UnionWithoutKeyVisitor) error {
	switch u.Type {
	default:
		return fmt.Errorf("invalid type %s in %T", u.Type, u)
	case "foo":
		return v.VisitFoo(u.Foo)
	case "bar":
		return v.VisitBar(u.Bar)
	}
}
