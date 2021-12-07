from datetime import datetime, date
import typing
from pydantic import BaseModel
from enum import Enum

from autonotion.models.blocks import TextBlock


class PropertyTypeEnum(Enum):
    RICHTEXT = "rich_text"
    NUMBER = "number"
    SELECT = "select"
    MULTISELECT = "multi_select"
    DATE = "date"
    FORMULA = "formula"
    RELATION = "relation"
    ROLLUP = "rollup"
    TITLE = "title"
    PEOPLE = "people"
    FILES = "files"
    CHECKBOX = "checkbox"
    URL = "url"
    EMAIL = "email"
    PHONE = "phone_number"
    CREATED_TIME = "created_time"
    CREATED_BY = "created_by"
    LAST_EDITED_TIME = "last_edited_time"
    LAST_EDITED_BY = "last_edited_by"


class ColorEnum:
    DEFAULT = "default"
    GRAY = "gray"
    BROWN = "brown"
    RED = "red"
    ORANGE = "orange"
    YELLOW = "yellow"
    GREEN = "green"
    BLUE = "blue"
    PURPLE = "purple"
    PINK = "pink"


class BaseProperty(BaseModel):
    id: str
    name: typing.Optional[str] = None
    type: str


class Formula(BaseModel):
    type: str
    string: typing.Optional[str]
    number: typing.Optional[float] = 0.0
    boolean: typing.Optional[bool] = False
    date: typing.Optional[datetime]


class SelectOption(BaseModel):
    id: str
    name: str
    color: typing.Optional[str] = ColorEnum.DEFAULT


class SelectProperty(BaseProperty):
    select: typing.Optional[SelectOption]


class MultiSelectProperty(BaseProperty):
    multi_select: typing.Optional[typing.List[SelectOption]]


class Date(BaseModel):
    start: date
    end: typing.Optional[date] = None


class DateProperty(BaseProperty):
    date: typing.Optional[Date]


class CreatedTime(BaseProperty):
    created_time: datetime


class FormulaProperty(BaseProperty):
    formula: typing.Optional[Formula]


class File(BaseModel):
    type: str
    url: str
    expiry_time: typing.Optional[datetime]


class People(BaseModel):
    id: str
    name: str
    avatar_url: typing.Optional[str] = None
    person: typing.Optional[typing.Dict[str, str]] = None


class PeopleProperty(BaseProperty):
    people: typing.Optional[typing.List[People]]


class TitleProperty(BaseProperty):
    title: typing.List[TextBlock]