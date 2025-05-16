# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ObjectListResponse", "Object"]


class Object(BaseModel):
    content_type: Optional[str] = None
    """
    **DESCRIPTION** MIME type of the object **REQUIRED** true **EXAMPLE**
    "application/pdf"
    """

    key: Optional[str] = None
    """
    **DESCRIPTION** Object key/path in the bucket **REQUIRED** true **EXAMPLE**
    "08036c5a50a93da84c5c45ba468c58159d75281e.pdf"
    """

    last_modified: Optional[datetime] = None
    """
    **DESCRIPTION** Last modification timestamp **REQUIRED** true **EXAMPLE**
    "2025-05-05T18:36:43.029Z"
    """

    size: Union[int, str, None] = None
    """
    **DESCRIPTION** Size of the object in bytes **REQUIRED** true **EXAMPLE** 401107
    """


class ObjectListResponse(BaseModel):
    objects: Optional[List[Object]] = None
    """
    **DESCRIPTION** List of objects in the bucket with their metadata **REQUIRED**
    true **EXAMPLE** [{"key": "08036c5a50a93da84c5c45ba468c58159d75281e.pdf",
    "size": "401107", "content_type": "application/pdf", "last_modified":
    "2025-05-05T18:36:43.029Z"}, {"key":
    "0a29925ccc5e6299e132a73325956a3abef6dd26.pdf", "size": "57173", "content_type":
    "application/pdf", "last_modified": "2025-05-05T18:36:43.985Z"}, {"key":
    "0e21835a42a6df2405496f62647058ff855743c1.pdf", "size": "1223197",
    "content_type": "application/pdf", "last_modified": "2025-05-05T18:36:45.362Z"}]
    """
