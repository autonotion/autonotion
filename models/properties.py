from typing import Optional, List
from datetime import datetime
import typing
from pydantic import BaseModel
from enum import Enum


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
    name: str
    type: str


class SelectOption(BaseModel):
    id: str
    name: str
    color: Optional[str] = ColorEnum.DEFAULT


class SelectProperty(BaseProperty):
    select: Optional[SelectOption]


class MultiSelectProperty(BaseProperty):
    multi_select: Optional[List[SelectOption]]


class DateProperty(BaseProperty):
    start: datetime
    end: Optional[datetime]


class Formula(BaseModel):
    type: str
    string: Optional[str]
    number: Optional[float] = 0.0
    boolean: Optional[bool] = False
    date: Optional[datetime]


class FormulaProperty(BaseProperty):
    string: str
    formula: Formula


Property = typing.Union[
    SelectProperty,
    MultiSelectProperty,
    DateProperty,
    FormulaProperty
]
