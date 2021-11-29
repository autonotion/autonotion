import typing
from datetime import datetime
from pydantic import BaseModel

from models.properties import Property


class Icon(BaseModel):
    type: str
    emoji: str


class BaseParent(BaseModel):
    type: str


class PageParent(BaseParent):
    page_id: str


class DatabaseParent(BaseParent):
    database_id: str


class WorkspaceParent(BaseParent):
    workspace: bool


class Page(BaseModel):
    _object: str
    id: str
    created_time: datetime
    last_edited_time: datetime
    archived: bool = False
    icon: typing.Optional[Icon]
    parent: typing.Union[PageParent, DatabaseParent, WorkspaceParent]
    property: typing.List[Property]
    url: str
