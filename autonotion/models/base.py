from autonotion.base import BaseMultiValueNotionObject, BaseNotionModel, BaseTypedNotionObject


class BaseIDNotionObject(BaseNotionModel):
    """
    Base class for all typed notion objects, it means object contains a property
    called `id` which is always string and it's required."""
    id: str


class ParentableNotionObject(BaseNotionModel):
    """
    Base class for all notion objects which can have a parent. As API v2.0 for Notion
    it's possible to have a notion object which is a child of a workspace, a database or
    a page.
    """
    parent: str


class BaseNotionObject(BaseIDNotionObject):
    """
    Base class for notion objects that belongs to a notion concept. As API v2.0 for Notion
    It's know that Database, Page and Person(User or Bots) are notion concepts."""
    object: str


class ContainerNotionObject(ParentableNotionObject, BaseNotionObject):
    """
    Base class for notion objects that can contain other notion objects. As API v2.0 for Notion
    It's know that Database and Page are notion containers."""
    pass


class BaseNotionProperty(BaseIDNotionObject, BaseTypedNotionObject):
    """
    Base class for notion properties. As API v2.0 for Notion Database and Page have properties
    with same user but different implementation."""
    name: str


class BaseDatabaseProperty(BaseNotionProperty):
    """
    As API v2.0 for Notion Database contains the properties that describes how pages that are
    contained in database will looks like."""
    pass


class BasePropertyInstance(BaseNotionProperty):
    """
    As API v2.0 for Notion all pages may contain properties, and this class holds the value of
    each property that container database has described if page is a database child."""
    pass


class BaseParentNotionObject(BaseTypedNotionObject):
    """
    Base class representation for parents object. As API v2.0 for Notion
    it's possible to have a notion object which is a child of a workspace, a database or
    a page."""
    pass


class BaseTypeMultiValueNotionObject(BaseMultiValueNotionObject, BaseTypedNotionObject):
    """
    Base class for notion objects that can have multiple type values. As API v2.0 for Notion
    formula is an example that may contain more than 1 type of value ."""
    def dict(self, *args, **kwargs):
        built = super().dict(*args, **kwargs)
        for key in set(built.keys()) - set(['type', self.type]):
            del built[key]
        return built


class BaseTypeMultiValueProperty(BaseTypeMultiValueNotionObject, BasePropertyInstance):
    """
    Base class for notion properties that can have multiple type values. As API v2.0 for Notion
    formula is an example that may contain more than 1 type of value ."""
    pass
