# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["StorageObjectUploadResponse"]


class StorageObjectUploadResponse(BaseModel):
    bucket_id: Optional[str] = None
    """ID of the bucket where the object was uploaded"""

    key: Optional[str] = None
    """Key/path of the uploaded object"""
