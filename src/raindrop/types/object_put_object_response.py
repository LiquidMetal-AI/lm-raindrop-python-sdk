# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .bucket_response import BucketResponse

__all__ = ["ObjectPutObjectResponse"]


class ObjectPutObjectResponse(BaseModel):
    bucket: Optional[BucketResponse] = None
    """Information about the bucket where the object was uploaded"""

    key: Optional[str] = None
    """Key/path of the uploaded object"""
