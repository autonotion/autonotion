import typing
from datetime import datetime, date

from autonotion.models.base import BaseTypeMultiValueNotionObject, BaseNotionModel


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


class Formula(BaseTypeMultiValueNotionObject):
    type: typing.Optional[str]
    string: typing.Optional[str]
    number: typing.Optional[float] = 0.0
    boolean: typing.Optional[bool] = False
    date: typing.Optional[datetime]


class FormulaExpression(BaseNotionModel):
    expression: str


class SelectOption(BaseNotionModel):
    id: str
    name: str
    color: typing.Optional[str] = ColorEnum.DEFAULT


class OptionGroup(BaseNotionModel):
    options: typing.List[SelectOption]


class Date(BaseNotionModel):
    start: typing.Optional[date]
    end: typing.Optional[date] = None
    time_zone: typing.Optional[str] = None

    def dict(self, *args, **kwargs):
        return {
            "start": datetime.strftime(self.start, "%Y-%m-%d") if self.start else None,
            "end": datetime.strftime(self.end, "%Y-%m-%d") if self.end else None,
            "time_zone": self.time_zone,
        }


class IconEmoji(BaseNotionModel):
    emoji: str


class External(BaseNotionModel):
    url: str


class File(BaseNotionModel):
    url: str
    expiry_time: typing.Optional[datetime]
