# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BucketResponse"]


class BucketResponse(BaseModel):
    application_name: Optional[str] = None

    application_version_id: Optional[str] = None

    bucket_name: Optional[str] = None

    module_id: Optional[str] = None
