from datetime import datetime, date, timezone
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

    class Config:
        json_encoders = {
            datetime: lambda v: v.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.000Z'),
            date: lambda v: v.strftime('%Y-%m-%dT%H:%M:%S.000Z'),
        }


class Formula(BaseModel):
    type: typing.Optional[str]
    string: typing.Optional[str]
    number: typing.Optional[float] = 0.0
    boolean: typing.Optional[bool] = False
    date: typing.Optional[datetime]

    def __init__(__pydantic_self__, **data: typing.Any) -> None:
        super().__init__(**data)
        for key in set(dict(__pydantic_self__).keys()) - set(data.keys()):
            delattr(__pydantic_self__, key)


class FormulaExpression(BaseModel):
    expression: str


class FormulaProperty(BaseProperty):
    formula: typing.Optional[FormulaExpression]


class FormulaPropertyInstance(BaseProperty):
    formula: typing.Optional[Formula]


class SelectOption(BaseModel):
    id: str
    name: str
    color: typing.Optional[str] = ColorEnum.DEFAULT


class OptionGroup(BaseModel):
    options: typing.List[SelectOption]


class SelectProperty(BaseProperty):
    select: typing.Optional[typing.Union[SelectOption, OptionGroup]]


class MultiSelectProperty(BaseProperty):
    multi_select: typing.Optional[typing.Union[typing.List[SelectOption], OptionGroup]]


class Date(BaseModel):
    start: typing.Optional[date]
    end: typing.Optional[date] = None


class DateProperty(BaseProperty):
    date: dict


class DatePropertyInstance(BaseProperty):
    date: typing.Optional[Date]


class CreatedTime(BaseProperty):
    created_time: typing.Union[datetime, dict]


class People(BaseProperty):
    avatar_url: typing.Optional[str] = None
    person: typing.Optional[typing.Dict[str, str]] = None
    object: typing.Optional[str] = "user"


class PeopleProperty(BaseProperty):
    people: typing.Optional[typing.Union[typing.List[People], dict]]


class TitleProperty(BaseProperty):
    title: typing.Union[typing.List[TextBlock], dict]


class IconEmoji(BaseModel):
    emoji: str


class External(BaseModel):
    url: str


class File(BaseModel):
    url: str
    type: typing.Optional[str]
    expiry_time: typing.Optional[datetime]

    def __init__(__pydantic_self__, **data: typing.Any) -> None:
        super().__init__(**data)
        for key in set(dict(__pydantic_self__).keys()) - set(data.keys()):
            delattr(__pydantic_self__, key)


class Icon(BaseModel):
    type: typing.Optional[str]
    file: typing.Optional[File]
    emoji: typing.Optional[IconEmoji]

    def __init__(__pydantic_self__, **data: typing.Any) -> None:
        super().__init__(**data)
        for key in set(dict(__pydantic_self__).keys()) - set(data.keys()):
            delattr(__pydantic_self__, key)


class CoverProperty(BaseModel):
    type: str
    file: typing.Optional[File]
    external: typing.Optional[External]

    def __init__(__pydantic_self__, **data: typing.Any) -> None:
        super().__init__(**data)
        for key in set(dict(__pydantic_self__).keys()) - set(data.keys()):
            delattr(__pydantic_self__, key)
