from .base import BaseParentNotionObject


class PageParent(BaseParentNotionObject):
    page_id: str


class DatabaseParent(BaseParentNotionObject):
    database_id: str


class WorkspaceParent(BaseParentNotionObject):
    workspace: bool
