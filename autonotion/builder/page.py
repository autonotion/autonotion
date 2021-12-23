import copy
from typing import get_type_hints

from autonotion.models.pages import Page
from autonotion.models.blocks import TextBlock

from .utils import NotionObjectBuilder, PAGE_TYPE, RawData
from .properties import CoverBuilder, PropertiesBuilder, IconBuilder, ParentBuilder

from autonotion.models.properties import (
    SelectProperty,
    MultiSelectProperty,
    DatePropertyInstance,
    FormulaPropertyInstance,
    CreatedTime,
    PeopleProperty,
    TitleProperty
)

BUILDER_CLASSES = {
    'select': SelectProperty,
    'multi_select': MultiSelectProperty,
    'date': DatePropertyInstance,
    'formula': FormulaPropertyInstance,
    'created_time': CreatedTime,
    'people': PeopleProperty,
    'title': TitleProperty,
    'text': TextBlock
}


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
        page.properties = PropertiesBuilder.build(
            _non_primitives['properties'],
            builder_class_map=BUILDER_CLASSES
        )
        page.cover = CoverBuilder.build(_non_primitives['cover'])
        return page
