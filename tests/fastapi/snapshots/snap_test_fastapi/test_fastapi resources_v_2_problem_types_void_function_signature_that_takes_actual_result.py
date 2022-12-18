# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ....commons.types.variable_type import VariableType
from .parameter import Parameter


class VoidFunctionSignatureThatTakesActualResult(pydantic.BaseModel):
    parameters: typing.List[Parameter]
    actual_result_type: VariableType = pydantic.Field(alias="actualResultType")

    class Partial(typing_extensions.TypedDict):
        parameters: typing_extensions.NotRequired[typing.List[Parameter]]
        actual_result_type: typing_extensions.NotRequired[VariableType]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @VoidFunctionSignatureThatTakesActualResult.Validators.root()
            def validate(values: VoidFunctionSignatureThatTakesActualResult.Partial) -> VoidFunctionSignatureThatTakesActualResult.Partial:
                ...

            @VoidFunctionSignatureThatTakesActualResult.Validators.field("parameters")
            def validate_parameters(parameters: typing.List[Parameter], values: VoidFunctionSignatureThatTakesActualResult.Partial) -> typing.List[Parameter]:
                ...

            @VoidFunctionSignatureThatTakesActualResult.Validators.field("actual_result_type")
            def validate_actual_result_type(actual_result_type: VariableType, values: VoidFunctionSignatureThatTakesActualResult.Partial) -> VariableType:
                ...
        """

        _pre_validators: typing.ClassVar[
            typing.List[VoidFunctionSignatureThatTakesActualResult.Validators._PreRootValidator]
        ] = []
        _post_validators: typing.ClassVar[
            typing.List[VoidFunctionSignatureThatTakesActualResult.Validators._RootValidator]
        ] = []
        _parameters_pre_validators: typing.ClassVar[
            typing.List[VoidFunctionSignatureThatTakesActualResult.Validators.PreParametersValidator]
        ] = []
        _parameters_post_validators: typing.ClassVar[
            typing.List[VoidFunctionSignatureThatTakesActualResult.Validators.ParametersValidator]
        ] = []
        _actual_result_type_pre_validators: typing.ClassVar[
            typing.List[VoidFunctionSignatureThatTakesActualResult.Validators.PreActualResultTypeValidator]
        ] = []
        _actual_result_type_post_validators: typing.ClassVar[
            typing.List[VoidFunctionSignatureThatTakesActualResult.Validators.ActualResultTypeValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [VoidFunctionSignatureThatTakesActualResult.Validators._RootValidator],
            VoidFunctionSignatureThatTakesActualResult.Validators._RootValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [VoidFunctionSignatureThatTakesActualResult.Validators._PreRootValidator],
            VoidFunctionSignatureThatTakesActualResult.Validators._PreRootValidator,
        ]:
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
            cls, field_name: typing_extensions.Literal["parameters"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [VoidFunctionSignatureThatTakesActualResult.Validators.PreParametersValidator],
            VoidFunctionSignatureThatTakesActualResult.Validators.PreParametersValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["parameters"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [VoidFunctionSignatureThatTakesActualResult.Validators.ParametersValidator],
            VoidFunctionSignatureThatTakesActualResult.Validators.ParametersValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["actual_result_type"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [VoidFunctionSignatureThatTakesActualResult.Validators.PreActualResultTypeValidator],
            VoidFunctionSignatureThatTakesActualResult.Validators.PreActualResultTypeValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["actual_result_type"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [VoidFunctionSignatureThatTakesActualResult.Validators.ActualResultTypeValidator],
            VoidFunctionSignatureThatTakesActualResult.Validators.ActualResultTypeValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "parameters":
                    if pre:
                        cls._parameters_pre_validators.append(validator)
                    else:
                        cls._parameters_post_validators.append(validator)
                if field_name == "actual_result_type":
                    if pre:
                        cls._actual_result_type_pre_validators.append(validator)
                    else:
                        cls._actual_result_type_post_validators.append(validator)
                return validator

            return decorator

        class PreParametersValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Any, __values: VoidFunctionSignatureThatTakesActualResult.Partial
            ) -> typing.Any:
                ...

        class ParametersValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.List[Parameter], __values: VoidFunctionSignatureThatTakesActualResult.Partial
            ) -> typing.List[Parameter]:
                ...

        class PreActualResultTypeValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Any, __values: VoidFunctionSignatureThatTakesActualResult.Partial
            ) -> typing.Any:
                ...

        class ActualResultTypeValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: VariableType, __values: VoidFunctionSignatureThatTakesActualResult.Partial
            ) -> VariableType:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(
                self, __values: VoidFunctionSignatureThatTakesActualResult.Partial
            ) -> VoidFunctionSignatureThatTakesActualResult.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(
        cls, values: VoidFunctionSignatureThatTakesActualResult.Partial
    ) -> VoidFunctionSignatureThatTakesActualResult.Partial:
        for validator in VoidFunctionSignatureThatTakesActualResult.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(
        cls, values: VoidFunctionSignatureThatTakesActualResult.Partial
    ) -> VoidFunctionSignatureThatTakesActualResult.Partial:
        for validator in VoidFunctionSignatureThatTakesActualResult.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("parameters", pre=True)
    def _pre_validate_parameters(
        cls, v: typing.List[Parameter], values: VoidFunctionSignatureThatTakesActualResult.Partial
    ) -> typing.List[Parameter]:
        for validator in VoidFunctionSignatureThatTakesActualResult.Validators._parameters_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("parameters", pre=False)
    def _post_validate_parameters(
        cls, v: typing.List[Parameter], values: VoidFunctionSignatureThatTakesActualResult.Partial
    ) -> typing.List[Parameter]:
        for validator in VoidFunctionSignatureThatTakesActualResult.Validators._parameters_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("actual_result_type", pre=True)
    def _pre_validate_actual_result_type(
        cls, v: VariableType, values: VoidFunctionSignatureThatTakesActualResult.Partial
    ) -> VariableType:
        for validator in VoidFunctionSignatureThatTakesActualResult.Validators._actual_result_type_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("actual_result_type", pre=False)
    def _post_validate_actual_result_type(
        cls, v: VariableType, values: VoidFunctionSignatureThatTakesActualResult.Partial
    ) -> VariableType:
        for validator in VoidFunctionSignatureThatTakesActualResult.Validators._actual_result_type_post_validators:
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
