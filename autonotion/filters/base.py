from autonotion.base import BaseMultiValueNotionObject


class BaseNotionFilter(BaseMultiValueNotionObject):
    """
    Base class for notion filters to query notion pages from databases."""
    property: str

    __slots__ = ('__filter_name__')

    def dict(self, *args, **kwargs) -> dict:
        body = dict([
            (key, val) for key, val in super().dict(*args, **kwargs).items() if key != 'property'
        ])

        return {
            'property': self.property,
            self.__filter_name__: body
        }


class BaseCompoundFilter(BaseMultiValueNotionObject):
    """
    Base class for compound filters.
    """
    pass
