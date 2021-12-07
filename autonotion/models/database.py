from typing import List, Optional, Union
from datetime import datetime
from pydantic import BaseModel
from autonotion.models.blocks import TextBlock

from autonotion.models.pages import Icon, PageParent, WorkspaceParent
from autonotion.models.properties import BaseProperty, File


class Database(BaseModel):
    """
    Database model
    """
    id: str
    created_time: datetime
    last_edited_time: datetime
    title: Optional[List[TextBlock]]
    icon: Optional[Union[Icon, File]]
    properties: Optional[List[BaseProperty]]
    parent: Optional[Union[PageParent, WorkspaceParent]]
    url: str
