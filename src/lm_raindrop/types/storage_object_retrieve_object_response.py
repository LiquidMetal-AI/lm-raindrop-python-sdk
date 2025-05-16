# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["StorageObjectRetrieveObjectResponse", "Bucket"]


class Bucket(BaseModel):
    application_name: Optional[str] = None

    application_version_id: Optional[str] = None

    bucket_name: Optional[str] = None

    module_id: Optional[str] = None


class StorageObjectRetrieveObjectResponse(BaseModel):
    bucket: Optional[Bucket] = None
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
