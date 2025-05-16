# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime

from .._models import BaseModel
from .bucket_response import BucketResponse

__all__ = ["ObjectRetrieveResponse"]


class ObjectRetrieveResponse(BaseModel):
    bucket: Optional[BucketResponse] = None
    """
    **DESCRIPTION** Information about the bucket where the object is stored
    **REQUIRED** true **EXAMPLE** {"module_id": "01jt3vs2nyt2xwk2f54x2bkn84",
    "bucket_name": "mr-bucket", "application_version_id":
    "01jt3vs1qggsy39eeyq4k295q1", "application_name": "demo-smartbucket"}
    """

    content_type: Optional[str] = None
    """
    **DESCRIPTION** MIME type of the object **REQUIRED** true **EXAMPLE**
    "application/pdf"
    """

    data: Optional[str] = None
    """
    **DESCRIPTION** The object data as a base64 encoded string **REQUIRED** true
    **EXAMPLE** "SGVsbG8gV29ybGQh"
    """

    key: Optional[str] = None
    """
    **DESCRIPTION** Key/path of the object **REQUIRED** true **EXAMPLE**
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
