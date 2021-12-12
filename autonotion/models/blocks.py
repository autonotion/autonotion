from typing import Optional
from pydantic import BaseModel
import pydantic


class Annotation(BaseModel):
    bold: Optional[bool] = False
    italic: Optional[bool] = False
    underline: Optional[bool] = False
    strikethrough: Optional[bool] = False
    code: Optional[bool] = False
    color: Optional[str] = "default"


class TextBlockContent(BaseModel):
    content: str
    link: Optional[pydantic.HttpUrl] = None


class TextBlock(BaseModel):
    type: str = 'text'
    text: TextBlockContent
    annotations: Optional[Annotation] = None
    plain_text: Optional[str] = ""
    href: Optional[pydantic.HttpUrl] = None
