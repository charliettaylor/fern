// This file was auto-generated by Fern from our API Definition.

package api

import (
	uuid "github.com/gofrs/uuid/v5"
)

// This is a Foo.
type Foo struct {
	Id   uuid.UUID `json:"id"`
	Name string    `json:"name"`
}
