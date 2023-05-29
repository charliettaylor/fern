package api

import (
	bar "github.com/fern-api/fern-go/internal/testdata/packages/generated/go/bar"
)

type Foo struct {
	Name  string   `json:"name"`
	Value *Value   `json:"value"`
	Bar   *bar.Bar `json:"bar"`
}
