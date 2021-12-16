from typing import List, Optional, Union
from datetime import datetime
from pydantic import BaseModel
from autonotion.models.blocks import TextBlock

from autonotion.models.base import BaseParentNotionObject
from autonotion.models.properties import BaseProperty, File, Icon


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
    parent: Optional[BaseParentNotionObject]
    url: str

    def dict(self, *args, **kwargs):
        """
        Convert model to dict
        """
        _dict = super().dict()
        _dict['object'] = 'database'
        if 'properties' in _dict.keys():
            _dict['properties'] = {
                prop.get('name'): prop for prop in _dict['properties']
            }
        return _dict
