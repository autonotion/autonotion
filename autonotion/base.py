import typing
from datetime import datetime, date, timezone

from pydantic import BaseModel


class BaseNotionModel(BaseModel):
    class Config:
        json_encoders = {
            datetime: lambda v: v.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.000Z'),
            date: lambda v: v.strftime('%Y-%m-%d'),
        }
        smart_union = True


class BaseTypedNotionObject(BaseNotionModel):
    """
    Base class for all typed notion objects, it means object contains a property
    called `type` which is always string and it's required.
    """
    type: str


class BaseMultiValueNotionObject(BaseNotionModel):
    """
    Base class for notion objects that can have multiple type values. As API v2.0 for Notion
    formula is an example that may contain more than 1 type of value ."""
    def __init__(__pydantic_self__, **data: typing.Any) -> None:
        super().__init__(**data)
        for key in set(dict(__pydantic_self__).keys()) - set(data.keys()):
            delattr(__pydantic_self__, key)


class BaseMultiTypeValueNotionObject(BaseMultiValueNotionObject, BaseTypedNotionObject):
    """
    Base class for notion objects that can have multiple type values. As API v2.0 for Notion
    formula is an example that may contain more than 1 type of value ."""
    pass
