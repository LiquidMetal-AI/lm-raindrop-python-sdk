# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .bucket_response import BucketResponse

__all__ = ["ObjectUploadResponse"]


class ObjectUploadResponse(BaseModel):
    bucket: Optional[BucketResponse] = None
    """
    **DESCRIPTION** Information about the bucket where the object was uploaded
    **REQUIRED** true **EXAMPLE** {"module_id": "01jt3vs2nyt2xwk2f54x2bkn84",
    "bucket_name": "mr-bucket", "application_version_id":
    "01jt3vs1qggsy39eeyq4k295q1", "application_name": "demo-smartbucket"}
    """

    key: Optional[str] = None
    """
    **DESCRIPTION** Key/path of the uploaded object **REQUIRED** true **EXAMPLE**
    "test-object.txt"
    """
