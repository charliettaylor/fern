# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from ...commons.types.problem_id import ProblemId
from ...commons.types.user_id import UserId
from .playlist_create_request import PlaylistCreateRequest
from .playlist_id import PlaylistId


class Playlist(PlaylistCreateRequest):
    playlist_id: PlaylistId
    owner_id: UserId = pydantic.Field(alias="owner-id")

    class Partial(PlaylistCreateRequest.Partial):
        playlist_id: typing_extensions.NotRequired[PlaylistId]
        owner_id: typing_extensions.NotRequired[UserId]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @Playlist.Validators.root()
            def validate(values: Playlist.Partial) -> Playlist.Partial:
                ...

            @Playlist.Validators.field("playlist_id")
            def validate_playlist_id(playlist_id: PlaylistId, values: Playlist.Partial) -> PlaylistId:
                ...

            @Playlist.Validators.field("owner_id")
            def validate_owner_id(owner_id: UserId, values: Playlist.Partial) -> UserId:
                ...

            @Playlist.Validators.field("name")
            def validate_name(name: str, values: Playlist.Partial) -> str:
                ...

            @Playlist.Validators.field("problems")
            def validate_problems(problems: typing.List[ProblemId], values: Playlist.Partial) -> typing.List[ProblemId]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[Playlist.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[Playlist.Validators._RootValidator]] = []
        _playlist_id_pre_validators: typing.ClassVar[typing.List[Playlist.Validators.PrePlaylistIdValidator]] = []
        _playlist_id_post_validators: typing.ClassVar[typing.List[Playlist.Validators.PlaylistIdValidator]] = []
        _owner_id_pre_validators: typing.ClassVar[typing.List[Playlist.Validators.PreOwnerIdValidator]] = []
        _owner_id_post_validators: typing.ClassVar[typing.List[Playlist.Validators.OwnerIdValidator]] = []
        _name_pre_validators: typing.ClassVar[typing.List[Playlist.Validators.PreNameValidator]] = []
        _name_post_validators: typing.ClassVar[typing.List[Playlist.Validators.NameValidator]] = []
        _problems_pre_validators: typing.ClassVar[typing.List[Playlist.Validators.PreProblemsValidator]] = []
        _problems_post_validators: typing.ClassVar[typing.List[Playlist.Validators.ProblemsValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Playlist.Validators._RootValidator], Playlist.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Playlist.Validators._PreRootValidator], Playlist.Validators._PreRootValidator]:
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
            cls, field_name: typing_extensions.Literal["playlist_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Playlist.Validators.PrePlaylistIdValidator], Playlist.Validators.PrePlaylistIdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["playlist_id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Playlist.Validators.PlaylistIdValidator], Playlist.Validators.PlaylistIdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["owner_id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Playlist.Validators.PreOwnerIdValidator], Playlist.Validators.PreOwnerIdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["owner_id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Playlist.Validators.OwnerIdValidator], Playlist.Validators.OwnerIdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Playlist.Validators.PreNameValidator], Playlist.Validators.PreNameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Playlist.Validators.NameValidator], Playlist.Validators.NameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problems"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Playlist.Validators.PreProblemsValidator], Playlist.Validators.PreProblemsValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["problems"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Playlist.Validators.ProblemsValidator], Playlist.Validators.ProblemsValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "playlist_id":
                    if pre:
                        cls._playlist_id_pre_validators.append(validator)
                    else:
                        cls._playlist_id_post_validators.append(validator)
                if field_name == "owner_id":
                    if pre:
                        cls._owner_id_pre_validators.append(validator)
                    else:
                        cls._owner_id_post_validators.append(validator)
                if field_name == "name":
                    if pre:
                        cls._name_pre_validators.append(validator)
                    else:
                        cls._name_post_validators.append(validator)
                if field_name == "problems":
                    if pre:
                        cls._problems_pre_validators.append(validator)
                    else:
                        cls._problems_post_validators.append(validator)
                return validator

            return decorator

        class PrePlaylistIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: Playlist.Partial) -> typing.Any:
                ...

        class PlaylistIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: PlaylistId, __values: Playlist.Partial) -> PlaylistId:
                ...

        class PreOwnerIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: Playlist.Partial) -> typing.Any:
                ...

        class OwnerIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: UserId, __values: Playlist.Partial) -> UserId:
                ...

        class PreNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: Playlist.Partial) -> typing.Any:
                ...

        class NameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: Playlist.Partial) -> str:
                ...

        class PreProblemsValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: Playlist.Partial) -> typing.Any:
                ...

        class ProblemsValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.List[ProblemId], __values: Playlist.Partial) -> typing.List[ProblemId]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: Playlist.Partial) -> Playlist.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: Playlist.Partial) -> Playlist.Partial:
        for validator in Playlist.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: Playlist.Partial) -> Playlist.Partial:
        for validator in Playlist.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("playlist_id", pre=True)
    def _pre_validate_playlist_id(cls, v: PlaylistId, values: Playlist.Partial) -> PlaylistId:
        for validator in Playlist.Validators._playlist_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("playlist_id", pre=False)
    def _post_validate_playlist_id(cls, v: PlaylistId, values: Playlist.Partial) -> PlaylistId:
        for validator in Playlist.Validators._playlist_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("owner_id", pre=True)
    def _pre_validate_owner_id(cls, v: UserId, values: Playlist.Partial) -> UserId:
        for validator in Playlist.Validators._owner_id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("owner_id", pre=False)
    def _post_validate_owner_id(cls, v: UserId, values: Playlist.Partial) -> UserId:
        for validator in Playlist.Validators._owner_id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("name", pre=True)
    def _pre_validate_name(cls, v: str, values: Playlist.Partial) -> str:
        v = super()._pre_validate_name(v, values)
        for validator in Playlist.Validators._name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("name", pre=False)
    def _post_validate_name(cls, v: str, values: Playlist.Partial) -> str:
        v = super()._post_validate_name(v, values)
        for validator in Playlist.Validators._name_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problems", pre=True)
    def _pre_validate_problems(cls, v: typing.List[ProblemId], values: Playlist.Partial) -> typing.List[ProblemId]:
        v = super()._pre_validate_problems(v, values)
        for validator in Playlist.Validators._problems_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("problems", pre=False)
    def _post_validate_problems(cls, v: typing.List[ProblemId], values: Playlist.Partial) -> typing.List[ProblemId]:
        v = super()._post_validate_problems(v, values)
        for validator in Playlist.Validators._problems_post_validators:
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
