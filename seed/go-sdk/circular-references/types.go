// This file was auto-generated by Fern from our API Definition.

package api

import (
	json "encoding/json"
	fmt "fmt"
	core "github.com/circular-references/fern/core"
)

type ImportingA struct {
	A *A `json:"a,omitempty" url:"a,omitempty"`

	_rawJSON json.RawMessage
}

func (i *ImportingA) UnmarshalJSON(data []byte) error {
	type unmarshaler ImportingA
	var value unmarshaler
	if err := json.Unmarshal(data, &value); err != nil {
		return err
	}
	*i = ImportingA(value)
	i._rawJSON = json.RawMessage(data)
	return nil
}

func (i *ImportingA) String() string {
	if len(i._rawJSON) > 0 {
		if value, err := core.StringifyJSON(i._rawJSON); err == nil {
			return value
		}
	}
	if value, err := core.StringifyJSON(i); err == nil {
		return value
	}
	return fmt.Sprintf("%#v", i)
}

type RootType struct {
	S string `json:"s" url:"s"`

	_rawJSON json.RawMessage
}

func (r *RootType) UnmarshalJSON(data []byte) error {
	type unmarshaler RootType
	var value unmarshaler
	if err := json.Unmarshal(data, &value); err != nil {
		return err
	}
	*r = RootType(value)
	r._rawJSON = json.RawMessage(data)
	return nil
}

func (r *RootType) String() string {
	if len(r._rawJSON) > 0 {
		if value, err := core.StringifyJSON(r._rawJSON); err == nil {
			return value
		}
	}
	if value, err := core.StringifyJSON(r); err == nil {
		return value
	}
	return fmt.Sprintf("%#v", r)
}

type A struct {
	S string `json:"s" url:"s"`

	_rawJSON json.RawMessage
}

func (a *A) UnmarshalJSON(data []byte) error {
	type unmarshaler A
	var value unmarshaler
	if err := json.Unmarshal(data, &value); err != nil {
		return err
	}
	*a = A(value)
	a._rawJSON = json.RawMessage(data)
	return nil
}

func (a *A) String() string {
	if len(a._rawJSON) > 0 {
		if value, err := core.StringifyJSON(a._rawJSON); err == nil {
			return value
		}
	}
	if value, err := core.StringifyJSON(a); err == nil {
		return value
	}
	return fmt.Sprintf("%#v", a)
}

type ContainerValue struct {
	Type     string
	List     []*FieldValue
	Optional *FieldValue
}

func NewContainerValueFromList(value []*FieldValue) *ContainerValue {
	return &ContainerValue{Type: "list", List: value}
}

func NewContainerValueFromOptional(value *FieldValue) *ContainerValue {
	return &ContainerValue{Type: "optional", Optional: value}
}

func (c *ContainerValue) UnmarshalJSON(data []byte) error {
	var unmarshaler struct {
		Type string `json:"type"`
	}
	if err := json.Unmarshal(data, &unmarshaler); err != nil {
		return err
	}
	c.Type = unmarshaler.Type
	switch unmarshaler.Type {
	case "list":
		var valueUnmarshaler struct {
			List []*FieldValue `json:"value,omitempty"`
		}
		if err := json.Unmarshal(data, &valueUnmarshaler); err != nil {
			return err
		}
		c.List = valueUnmarshaler.List
	case "optional":
		var valueUnmarshaler struct {
			Optional *FieldValue `json:"value,omitempty"`
		}
		if err := json.Unmarshal(data, &valueUnmarshaler); err != nil {
			return err
		}
		c.Optional = valueUnmarshaler.Optional
	}
	return nil
}

func (c ContainerValue) MarshalJSON() ([]byte, error) {
	switch c.Type {
	default:
		return nil, fmt.Errorf("invalid type %s in %T", c.Type, c)
	case "list":
		var marshaler = struct {
			Type string        `json:"type"`
			List []*FieldValue `json:"value,omitempty"`
		}{
			Type: "list",
			List: c.List,
		}
		return json.Marshal(marshaler)
	case "optional":
		var marshaler = struct {
			Type     string      `json:"type"`
			Optional *FieldValue `json:"value,omitempty"`
		}{
			Type:     "optional",
			Optional: c.Optional,
		}
		return json.Marshal(marshaler)
	}
}

type ContainerValueVisitor interface {
	VisitList([]*FieldValue) error
	VisitOptional(*FieldValue) error
}

func (c *ContainerValue) Accept(visitor ContainerValueVisitor) error {
	switch c.Type {
	default:
		return fmt.Errorf("invalid type %s in %T", c.Type, c)
	case "list":
		return visitor.VisitList(c.List)
	case "optional":
		return visitor.VisitOptional(c.Optional)
	}
}

type FieldValue struct {
	Type           string
	PrimitiveValue PrimitiveValue
	ObjectValue    *ObjectValue
	ContainerValue *ContainerValue
}

func NewFieldValueFromPrimitiveValue(value PrimitiveValue) *FieldValue {
	return &FieldValue{Type: "primitive_value", PrimitiveValue: value}
}

func NewFieldValueFromObjectValue(value *ObjectValue) *FieldValue {
	return &FieldValue{Type: "object_value", ObjectValue: value}
}

func NewFieldValueFromContainerValue(value *ContainerValue) *FieldValue {
	return &FieldValue{Type: "container_value", ContainerValue: value}
}

func (f *FieldValue) UnmarshalJSON(data []byte) error {
	var unmarshaler struct {
		Type string `json:"type"`
	}
	if err := json.Unmarshal(data, &unmarshaler); err != nil {
		return err
	}
	f.Type = unmarshaler.Type
	switch unmarshaler.Type {
	case "primitive_value":
		var valueUnmarshaler struct {
			PrimitiveValue PrimitiveValue `json:"value"`
		}
		if err := json.Unmarshal(data, &valueUnmarshaler); err != nil {
			return err
		}
		f.PrimitiveValue = valueUnmarshaler.PrimitiveValue
	case "object_value":
		value := new(ObjectValue)
		if err := json.Unmarshal(data, &value); err != nil {
			return err
		}
		f.ObjectValue = value
	case "container_value":
		var valueUnmarshaler struct {
			ContainerValue *ContainerValue `json:"value,omitempty"`
		}
		if err := json.Unmarshal(data, &valueUnmarshaler); err != nil {
			return err
		}
		f.ContainerValue = valueUnmarshaler.ContainerValue
	}
	return nil
}

func (f FieldValue) MarshalJSON() ([]byte, error) {
	switch f.Type {
	default:
		return nil, fmt.Errorf("invalid type %s in %T", f.Type, f)
	case "primitive_value":
		var marshaler = struct {
			Type           string         `json:"type"`
			PrimitiveValue PrimitiveValue `json:"value"`
		}{
			Type:           "primitive_value",
			PrimitiveValue: f.PrimitiveValue,
		}
		return json.Marshal(marshaler)
	case "object_value":
		var marshaler = struct {
			Type string `json:"type"`
			*ObjectValue
		}{
			Type:        "object_value",
			ObjectValue: f.ObjectValue,
		}
		return json.Marshal(marshaler)
	case "container_value":
		var marshaler = struct {
			Type           string          `json:"type"`
			ContainerValue *ContainerValue `json:"value,omitempty"`
		}{
			Type:           "container_value",
			ContainerValue: f.ContainerValue,
		}
		return json.Marshal(marshaler)
	}
}

type FieldValueVisitor interface {
	VisitPrimitiveValue(PrimitiveValue) error
	VisitObjectValue(*ObjectValue) error
	VisitContainerValue(*ContainerValue) error
}

func (f *FieldValue) Accept(visitor FieldValueVisitor) error {
	switch f.Type {
	default:
		return fmt.Errorf("invalid type %s in %T", f.Type, f)
	case "primitive_value":
		return visitor.VisitPrimitiveValue(f.PrimitiveValue)
	case "object_value":
		return visitor.VisitObjectValue(f.ObjectValue)
	case "container_value":
		return visitor.VisitContainerValue(f.ContainerValue)
	}
}

type ObjectValue struct {
	_rawJSON json.RawMessage
}

func (o *ObjectValue) UnmarshalJSON(data []byte) error {
	type unmarshaler ObjectValue
	var value unmarshaler
	if err := json.Unmarshal(data, &value); err != nil {
		return err
	}
	*o = ObjectValue(value)
	o._rawJSON = json.RawMessage(data)
	return nil
}

func (o *ObjectValue) String() string {
	if len(o._rawJSON) > 0 {
		if value, err := core.StringifyJSON(o._rawJSON); err == nil {
			return value
		}
	}
	if value, err := core.StringifyJSON(o); err == nil {
		return value
	}
	return fmt.Sprintf("%#v", o)
}

type PrimitiveValue string

const (
	PrimitiveValueString PrimitiveValue = "STRING"
	PrimitiveValueNumber PrimitiveValue = "NUMBER"
)

func NewPrimitiveValueFromString(s string) (PrimitiveValue, error) {
	switch s {
	case "STRING":
		return PrimitiveValueString, nil
	case "NUMBER":
		return PrimitiveValueNumber, nil
	}
	var t PrimitiveValue
	return "", fmt.Errorf("%s is not a valid %T", s, t)
}

func (p PrimitiveValue) Ptr() *PrimitiveValue {
	return &p
}
