from contextlib import AbstractContextManager
from typing import Any, TypeVar, overload
from typing_extensions import Literal

from .client import Pipeline, Redis, _StrType

_T = TypeVar("_T")

HIREDIS_AVAILABLE: bool

@overload
def from_url(url: str, *, db: int = ..., decode_responses: Literal[True], **kwargs: Any) -> Redis[str]: ...
@overload
def from_url(url: str, *, db: int = ..., decode_responses: Literal[False] = ..., **kwargs: Any) -> Redis[bytes]: ...
def pipeline(redis_obj: Redis[_StrType]) -> AbstractContextManager[Pipeline[_StrType]]: ...
@overload
def str_if_bytes(value: bytes) -> str: ...  # type: ignore[misc]
@overload
def str_if_bytes(value: _T) -> _T: ...
def safe_str(value: object) -> str: ...
