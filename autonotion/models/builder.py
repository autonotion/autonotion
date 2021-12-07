import copy
from typing import get_type_hints, Dict

from autonotion.models.pages import Page, Icon, PageParent, DatabaseParent
from autonotion.models.database import Database
from autonotion.models.properties import (
    BaseProperty,
    SelectProperty,
    MultiSelectProperty,
    DateProperty,
    FormulaProperty,
    CreatedTime,
    PeopleProperty,
    TitleProperty
)


PAGE_TYPE = Page
DATABASE_TYPE = Database


ROOT_TYPES = {
    'page': PAGE_TYPE,
    'database': DATABASE_TYPE
}

RawData = Dict[str, str]


class NotionObjectBuilder(object):
    """
    Base class for all builders.
    """

    def build(self):
        """
        Builds the notion object.
        """
        raise NotImplementedError


class PageBuilder(NotionObjectBuilder):
    """
    Builds a page.
    """
    @classmethod
    def build(cls, data: RawData) -> Page:
        """
        Builds a page.
        """
        _raw_data = {}
        _non_primitives = {}
        for k, v in get_type_hints(PAGE_TYPE).items():
            if not k.startswith('_'):
                if isinstance(v, type):
                    _raw_data[k] = data[k]
                else:
                    _non_primitives[k] = copy.deepcopy(data[k])
                    del data[k]

        page = PAGE_TYPE.parse_obj(_raw_data)
        page.icon = IconBuilder.build(_non_primitives['icon'])
        page.parent = ParentBuilder.build(_non_primitives['parent'])
        page.properties = PropertiesBuilder.build(_non_primitives['properties'])
        return page


class IconBuilder(NotionObjectBuilder):
    """
    Builds an icon.
    """
    @classmethod
    def build(cls, data: RawData) -> str:
        """
        Builds an icon.
        """
        if not data:
            return None
        return Icon.parse_obj(data)


class ParentBuilder(NotionObjectBuilder):
    """
    Builds a parent.
    """
    @classmethod
    def build(cls, data: RawData) -> str:
        """
        Builds a parent.
        """
        class_ = {
            'page_id': PageParent,
            'database_id': DatabaseParent
        }
        return class_[data['type']].parse_obj(data)


class PropertiesBuilder(NotionObjectBuilder):
    """
    Builds properties.
    """
    @classmethod
    def build(cls, data: RawData) -> Dict[str, str]:
        """
        Builds properties.
        """
        return [PropertyBuilder.build(**{'name': k, 'data': v}) for k, v in data.items()]


class PropertyBuilder(NotionObjectBuilder):
    """
    Builds a property.
    """
    @classmethod
    def build(cls, name: str, data: RawData) -> BaseProperty:
        """
        Builds a property.
        """
        class_types = {
            'select': SelectProperty,
            'multi_select': MultiSelectProperty,
            'date': DateProperty,
            'formula': FormulaProperty,
            'created_time': CreatedTime,
            'people': PeopleProperty,
            'title': TitleProperty
        }
        _type = data['type']
        _class = class_types[_type]
        data.update({'name': name})
        return _class.parse_obj(data)
