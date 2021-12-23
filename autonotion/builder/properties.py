from typing import Dict

from autonotion.models.base import BaseNotionProperty
from autonotion.models.pages import Icon
from autonotion.models.parents import PageParent, DatabaseParent, WorkspaceParent
from autonotion.models.properties import CoverProperty

from .utils import NotionObjectBuilder, RawData


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
            'database_id': DatabaseParent,
            'workspace': WorkspaceParent
        }
        return class_[data['type']].parse_obj(data)


class PropertiesBuilder(NotionObjectBuilder):
    """
    Builds properties.
    """
    @classmethod
    def build(
            cls,
            data: RawData,
            builder_class_map: Dict[str, BaseNotionProperty]) -> Dict[str, str]:
        """
        Builds properties.
        """
        return [PropertyBuilder.build(**{
            'name': k,
            'data': v,
            'builder_class': builder_class_map[v['type']]
            }) for k, v in data.items()]


class PropertyBuilder(NotionObjectBuilder):
    """
    Builds a property.
    """
    @classmethod
    def build(
        cls,
        name: str,
        data: RawData,
        builder_class: BaseNotionProperty
    ) -> BaseNotionProperty:
        """
        Builds a property.
        """
        if isinstance(data, list):
            instances = []
            for row in data:
                row.update({'name': name})
                instances.append(builder_class.parse_obj(row))
            return instances

        else:
            _class = builder_class
            data.update({'name': name})
            return _class.parse_obj(data)


class CoverBuilder(NotionObjectBuilder):
    """
    Builds a cover.
    """
    @classmethod
    def build(cls, data: RawData) -> str:
        """
        Builds a cover.
        """
        if not data:
            return None
        return CoverProperty.parse_obj(data)
