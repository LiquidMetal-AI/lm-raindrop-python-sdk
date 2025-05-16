# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime

from .._models import BaseModel
from .bucket_response import BucketResponse

__all__ = ["ObjectRetrieveObjectResponse"]


class ObjectRetrieveObjectResponse(BaseModel):
    bucket: Optional[BucketResponse] = None
    """Information about the bucket where the object is stored"""

    content_type: Optional[str] = None
    """MIME type of the object"""

    data: Optional[str] = None
    """The object data as a base64 encoded string"""

    key: Optional[str] = None
    """Key/path of the object"""

    last_modified: Optional[datetime] = None
    """Last modification timestamp"""

    size: Union[int, str, None] = None
    """Size of the object in bytes"""
