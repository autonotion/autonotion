from datetime import datetime
import typing
from enum import Enum

from autonotion.models.base import BaseTypeMultiValueNotionObject, BaseNotionProperty
from autonotion.models.objects import (
    Formula,
    FormulaExpression,
    SelectOption,
    OptionGroup,
    Date,
    IconEmoji,
    External
)

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


class FormulaProperty(BaseNotionProperty):
    formula: typing.Optional[FormulaExpression]


class FormulaPropertyInstance(BaseNotionProperty):
    formula: typing.Optional[Formula]


class SelectProperty(BaseNotionProperty):
    select: typing.Optional[typing.Union[SelectOption, OptionGroup]]


class MultiSelectProperty(BaseNotionProperty):
    multi_select: typing.Optional[typing.Union[typing.List[SelectOption], OptionGroup]]


class DateProperty(BaseNotionProperty):
    date: dict


class DatePropertyInstance(BaseNotionProperty):
    date: typing.Optional[Date]


class CreatedTime(BaseNotionProperty):
    created_time: typing.Union[datetime, dict]


class People(BaseNotionProperty):
    avatar_url: typing.Optional[str] = None
    person: typing.Optional[typing.Dict[str, str]] = None
    object: typing.Optional[str] = "user"


class PeopleProperty(BaseNotionProperty):
    people: typing.Optional[typing.Union[typing.List[People], dict]]


class TitleProperty(BaseNotionProperty):
    title: typing.Union[typing.List[TextBlock], dict]


class File(BaseTypeMultiValueNotionObject):
    url: str
    expiry_time: typing.Optional[datetime]


class Icon(BaseTypeMultiValueNotionObject):
    file: typing.Optional[File]
    emoji: typing.Optional[IconEmoji]


class CoverProperty(BaseTypeMultiValueNotionObject):
    file: typing.Optional[File]
    external: typing.Optional[External]
