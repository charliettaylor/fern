# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class ListType(pydantic.BaseModel):
    value_type: VariableType = pydantic.Field(alias="valueType")
    is_fixed_length: typing.Optional[bool] = pydantic.Field(
        alias="isFixedLength",
        description=(
            "Whether this list is fixed-size (for languages that supports fixed-size lists). Defaults to false.\n"
        ),
    )

    class Partial(typing_extensions.TypedDict):
        value_type: typing_extensions.NotRequired[VariableType]
        is_fixed_length: typing_extensions.NotRequired[typing.Optional[bool]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ListType.Validators.root()
            def validate(values: ListType.Partial) -> ListType.Partial:
                ...

            @ListType.Validators.field("value_type")
            def validate_value_type(value_type: VariableType, values: ListType.Partial) -> VariableType:
                ...

            @ListType.Validators.field("is_fixed_length")
            def validate_is_fixed_length(is_fixed_length: typing.Optional[bool], values: ListType.Partial) -> typing.Optional[bool]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[ListType.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[ListType.Validators._RootValidator]] = []
        _value_type_pre_validators: typing.ClassVar[typing.List[ListType.Validators.PreValueTypeValidator]] = []
        _value_type_post_validators: typing.ClassVar[typing.List[ListType.Validators.ValueTypeValidator]] = []
        _is_fixed_length_pre_validators: typing.ClassVar[
            typing.List[ListType.Validators.PreIsFixedLengthValidator]
        ] = []
        _is_fixed_length_post_validators: typing.ClassVar[typing.List[ListType.Validators.IsFixedLengthValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[ListType.Validators._RootValidator], ListType.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[ListType.Validators._PreRootValidator], ListType.Validators._PreRootValidator]:
            ...

        @classmethod
        def root(cls, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["value_type"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[ListType.Validators.PreValueTypeValidator], ListType.Validators.PreValueTypeValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["value_type"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[ListType.Validators.ValueTypeValidator], ListType.Validators.ValueTypeValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["is_fixed_length"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ListType.Validators.PreIsFixedLengthValidator], ListType.Validators.PreIsFixedLengthValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["is_fixed_length"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[[ListType.Validators.IsFixedLengthValidator], ListType.Validators.IsFixedLengthValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "value_type":
                    if pre:
                        cls._value_type_pre_validators.append(validator)
                    else:
                        cls._value_type_post_validators.append(validator)
                if field_name == "is_fixed_length":
                    if pre:
                        cls._is_fixed_length_pre_validators.append(validator)
                    else:
                        cls._is_fixed_length_post_validators.append(validator)
                return validator

            return decorator

        class PreValueTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ListType.Partial) -> typing.Any:
                ...

        class ValueTypeValidator(typing_extensions.Protocol):
            def __call__(self, __v: VariableType, __values: ListType.Partial) -> VariableType:
                ...

        class PreIsFixedLengthValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ListType.Partial) -> typing.Any:
                ...

        class IsFixedLengthValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Optional[bool], __values: ListType.Partial) -> typing.Optional[bool]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: ListType.Partial) -> ListType.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: ListType.Partial) -> ListType.Partial:
        for validator in ListType.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: ListType.Partial) -> ListType.Partial:
        for validator in ListType.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("value_type", pre=True)
    def _pre_validate_value_type(cls, v: VariableType, values: ListType.Partial) -> VariableType:
        for validator in ListType.Validators._value_type_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("value_type", pre=False)
    def _post_validate_value_type(cls, v: VariableType, values: ListType.Partial) -> VariableType:
        for validator in ListType.Validators._value_type_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("is_fixed_length", pre=True)
    def _pre_validate_is_fixed_length(cls, v: typing.Optional[bool], values: ListType.Partial) -> typing.Optional[bool]:
        for validator in ListType.Validators._is_fixed_length_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("is_fixed_length", pre=False)
    def _post_validate_is_fixed_length(
        cls, v: typing.Optional[bool], values: ListType.Partial
    ) -> typing.Optional[bool]:
        for validator in ListType.Validators._is_fixed_length_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        extra = pydantic.Extra.forbid


from .variable_type import VariableType  # noqa: E402

ListType.update_forward_refs()
