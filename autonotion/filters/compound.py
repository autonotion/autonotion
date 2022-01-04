import typing

from autonotion.filters.base import BaseCompoundFilter, BaseNotionFilter


class CompoundFilter(BaseCompoundFilter):
    """
    Base class for compound filters.
    """
    and_: typing.Optional[typing.List[BaseNotionFilter]]
    or_: typing.Optional[typing.List[BaseNotionFilter]]

    def __init__(__pydantic_self__, **data: typing.Any) -> None:
        has_and = 'and_' in data and data['and_']
        has_or = 'or_' in data and data['or_']
        if has_and and has_or:
            raise ValueError("CompoundFilter can't have both 'and_' and 'or_'")

        super().__init__(**data)

    def dict(self, *args, **kwargs):
        d = {}
        if hasattr(self, "and_") and self.and_:
            d["and"] = [f.dict() for f in self.and_]
        if hasattr(self, "or_") and self.or_:
            d["or"] = [f.dict() for f in self.or_]
        return d
