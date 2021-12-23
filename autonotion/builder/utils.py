from typing import Dict

from autonotion.models.pages import Page
from autonotion.models.database import Database

PAGE_TYPE = Page
DATABASE_TYPE = Database

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
