import typing
from datetime import datetime, date

from autonotion.filters.base import BaseNotionFilter


class TextNotionFilter(BaseNotionFilter):
    """
    Filter for text property.
    """
    __filter_name__: str = 'text'

    equals: typing.Optional[str]
    does_not_equal: typing.Optional[str]
    contains: typing.Optional[str]
    starts_with: typing.Optional[str]
    ends_with: typing.Optional[str]
    is_empty: typing.Optional[bool]
    is_not_empty: typing.Optional[bool]


class NumberNotionFilter(BaseNotionFilter):
    """
    Filter for number property.
    """
    __filter_name__: str = 'number'

    equals: typing.Optional[typing.Union[float, int]]
    does_not_equal: typing.Optional[typing.Union[float, int]]
    greater_than: typing.Optional[typing.Union[float, int]]
    greater_than_or_equal: typing.Optional[typing.Union[float, int]]
    less_than: typing.Optional[typing.Union[float, int]]
    less_than_or_equal: typing.Optional[typing.Union[float, int]]
    is_empty: typing.Optional[bool]
    is_not_empty: typing.Optional[bool]


class CheckboxNotionFilter(BaseNotionFilter):
    """
    Filter for checkbox property.
    """
    __filter_name__: str = 'checkbox'

    equals: typing.Optional[bool]
    does_not_equal: typing.Optional[bool]


class SelectNotionFilter(BaseNotionFilter):
    """
    Filter for select property.
    """
    __filter_name__: str = 'select'

    equals: typing.Optional[str]
    does_not_equal: typing.Optional[str]
    is_empty: typing.Optional[bool]
    is_not_empty: typing.Optional[bool]


class MultiSelectNotionFilter(BaseNotionFilter):
    """
    Filter for multi select property.
    """
    __filter_name__: str = 'multiselect'

    contains: typing.Optional[str]
    does_not_contain: typing.Optional[str]
    is_empty: typing.Optional[bool]
    is_not_empty: typing.Optional[bool]


class DateTimeNotionFilter(BaseNotionFilter):
    """
    Filter for date time property.
    """
    __filter_name__: str = 'datetime'

    equals: typing.Optional[typing.Union[datetime, date]]
    before: typing.Optional[typing.Union[datetime, date]]
    after: typing.Optional[typing.Union[datetime, date]]
    on_or_before: typing.Optional[typing.Union[datetime, date]]
    on_or_after: typing.Optional[typing.Union[datetime, date]]
    is_empty: typing.Optional[bool]
    is_not_empty: typing.Optional[bool]
    past_week: typing.Optional[bool]
    past_month: typing.Optional[bool]
    past_year: typing.Optional[bool]
    next_week: typing.Optional[bool]
    next_month: typing.Optional[bool]
    next_year: typing.Optional[bool]

    __translate_fields__ = [
        'past_week',
        'past_month',
        'past_year',
        'next_week',
        'next_month',
        'next_year'
    ]

    def dict(self, *args, **kwargs) -> typing.Dict[str, typing.Any]:
        data = super().dict()
        for field in self.__translate_fields__:
            if data.get(self.__filter_name__).get(field):
                data[self.__filter_name__][field] = {}
        return data


class PersonNotionFilter(BaseNotionFilter):
    """
    Filter for person property.
    """
    __filter_name__: str = 'person'

    contains: typing.Optional[str]
    does_not_contain: typing.Optional[str]
    is_empty: typing.Optional[bool]
    is_not_empty: typing.Optional[bool]


class FileNotionFilter(BaseNotionFilter):
    """
    Filter for file property.
    """
    __filter_name__: str = 'file'

    is_empty: typing.Optional[bool]
    is_not_empty: typing.Optional[bool]


class FormulaNotionFilter(BaseNotionFilter):
    """
    Filter for formula property.
    """
    __filter_name__: str = 'formula'

    text: typing.Optional[str]
    checkbox: typing.Optional[bool]
    number: typing.Optional[typing.Union[float, int]]
    date: typing.Optional[typing.Union[datetime, date]]
