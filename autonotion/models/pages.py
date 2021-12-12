import typing
from datetime import datetime, date, timezone
from pydantic import BaseModel, validator

from autonotion.models.properties import BaseProperty


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
    object: str
    id: str
    created_time: datetime
    last_edited_time: datetime
    archived: bool = False
    icon: typing.Optional[Icon] = None
    parent: typing.Optional[
                typing.Union[
                    PageParent,
                    DatabaseParent,
                    WorkspaceParent
                ]
            ]
    properties: typing.Optional[typing.List[BaseProperty]]
    url: str

    class Config:
        json_encoders = {
            datetime: lambda v: v.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.000Z'),
            date: lambda v: v.strftime('%Y-%m-%dT%H:%M:%S.000Z'),
        }

    @validator('object')
    def object_should_be_page(cls, v):
        if v != 'page':
            raise ValueError('object should be page')
        return v

    def dict(self, *args, **kwargs):
        """
        Convert model to dict
        """
        _dict = super().dict()
        _dict['object'] = 'page'
        if 'properties' in _dict.keys():
            _dict['properties'] = {
                prop.pop('name'): prop for prop in _dict['properties']
            }
        return _dict

    
