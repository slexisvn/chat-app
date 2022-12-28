from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateUserRequest(_message.Message):
    __slots__ = ["User"]
    USER_FIELD_NUMBER: _ClassVar[int]
    User: User
    def __init__(self, User: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ["username"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    username: str
    def __init__(self, username: _Optional[str] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ["User"]
    USER_FIELD_NUMBER: _ClassVar[int]
    User: User
    def __init__(self, User: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ["_id", "username"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    _ID_FIELD_NUMBER: _ClassVar[int]
    _id: str
    username: str
    def __init__(self, _id: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...
