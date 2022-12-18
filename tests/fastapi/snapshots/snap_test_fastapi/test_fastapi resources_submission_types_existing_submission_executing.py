# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .submission_id import SubmissionId


class ExistingSubmissionExecuting(pydantic.BaseModel):
    submission_id: SubmissionId = pydantic.Field(alias="submissionId")

    class Partial(typing_extensions.TypedDict):
        submission_id: typing_extensions.NotRequired[SubmissionId]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @ExistingSubmissionExecuting.Validators.root()
            def validate(values: ExistingSubmissionExecuting.Partial) -> ExistingSubmissionExecuting.Partial:
                ...

            @ExistingSubmissionExecuting.Validators.field("submission_id")
            def validate_submission_id(submission_id: SubmissionId, values: ExistingSubmissionExecuting.Partial) -> SubmissionId:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[ExistingSubmissionExecuting.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[ExistingSubmissionExecuting.Validators._RootValidator]] = []
        _submission_id_pre_validators: typing.ClassVar[
            typing.List[ExistingSubmissionExecuting.Validators.PreSubmissionIdValidator]
        ] = []
        _submission_id_post_validators: typing.ClassVar[
            typing.List[ExistingSubmissionExecuting.Validators.SubmissionIdValidator]
        ] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [ExistingSubmissionExecuting.Validators._RootValidator],
            ExistingSubmissionExecuting.Validators._RootValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ExistingSubmissionExecuting.Validators._PreRootValidator],
            ExistingSubmissionExecuting.Validators._PreRootValidator,
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
            cls, field_name: typing_extensions.Literal["submission_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [ExistingSubmissionExecuting.Validators.PreSubmissionIdValidator],
            ExistingSubmissionExecuting.Validators.PreSubmissionIdValidator,
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls,
            field_name: typing_extensions.Literal["submission_id"],
            *,
            pre: typing_extensions.Literal[False] = False,
        ) -> typing.Callable[
            [ExistingSubmissionExecuting.Validators.SubmissionIdValidator],
            ExistingSubmissionExecuting.Validators.SubmissionIdValidator,
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "submission_id":
                    if pre:
                        cls._submission_id_pre_validators.append(validator)
                    else:
                        cls._submission_id_post_validators.append(validator)
                return validator

            return decorator

        class PreSubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: ExistingSubmissionExecuting.Partial) -> typing.Any:
                ...

        class SubmissionIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: SubmissionId, __values: ExistingSubmissionExecuting.Partial) -> SubmissionId:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: ExistingSubmissionExecuting.Partial) -> ExistingSubmissionExecuting.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: ExistingSubmissionExecuting.Partial) -> ExistingSubmissionExecuting.Partial:
        for validator in ExistingSubmissionExecuting.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: ExistingSubmissionExecuting.Partial) -> ExistingSubmissionExecuting.Partial:
        for validator in ExistingSubmissionExecuting.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("submission_id", pre=True)
    def _pre_validate_submission_id(cls, v: SubmissionId, values: ExistingSubmissionExecuting.Partial) -> SubmissionId:
        for validator in ExistingSubmissionExecuting.Validators._submission_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("submission_id", pre=False)
    def _post_validate_submission_id(cls, v: SubmissionId, values: ExistingSubmissionExecuting.Partial) -> SubmissionId:
        for validator in ExistingSubmissionExecuting.Validators._submission_id_post_validators:
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
