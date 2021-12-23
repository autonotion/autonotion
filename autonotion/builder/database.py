import copy
import logging
from typing import get_type_hints

from autonotion.models.database import Database
from autonotion.models.blocks import TextBlock

from .utils import NotionObjectBuilder, RawData, DATABASE_TYPE
from .properties import PropertyBuilder, PropertiesBuilder, ParentBuilder

from autonotion.models.properties import (
    SelectProperty,
    MultiSelectProperty,
    DateProperty,
    FormulaProperty,
    CreatedTime,
    PeopleProperty,
    TitleProperty
)


logger = logging.getLogger(__name__)

BUILDER_CLASSES = {
    'select': SelectProperty,
    'multi_select': MultiSelectProperty,
    'date': DateProperty,
    'formula': FormulaProperty,
    'created_time': CreatedTime,
    'people': PeopleProperty,
    'title': TitleProperty,
    'text': TextBlock
}


class DatabaseBuilder(NotionObjectBuilder):
    """
    Builds a database.
    """
    @classmethod
    def build(cls, data: RawData) -> Database:
        """
        Builds a database.
        """

        if not data.get('object') == 'database':
            logger.error(f'Expected database, got {data}')
            raise ValueError('Seems data does not contain a database.')

        _raw_data = {}
        _non_primitives = {}
        for k, v in get_type_hints(DATABASE_TYPE).items():
            if not k.startswith('_'):
                if isinstance(v, type):
                    _raw_data[k] = data[k]
                else:
                    _non_primitives[k] = copy.deepcopy(data[k])
                    del data[k]

        database = DATABASE_TYPE.parse_obj(_raw_data)
        database.parent = ParentBuilder.build(_non_primitives['parent'])
        database.properties = PropertiesBuilder.build(
            _non_primitives['properties'],
            builder_class_map=BUILDER_CLASSES
        )
        database.title = PropertyBuilder.build("title", _non_primitives['title'], TextBlock)
        return database
