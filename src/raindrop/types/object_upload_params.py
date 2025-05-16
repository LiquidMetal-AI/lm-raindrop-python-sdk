# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypedDict

from .._types import Base64FileInput
from .._utils import PropertyInfo

__all__ = ["ObjectUploadParams"]


class ObjectUploadParams(TypedDict, total=False):
    bucket_name: Required[str]

    content: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """**DESCRIPTION** Binary content of the object **REQUIRED** true"""

    content_type: str
    """
    **DESCRIPTION** MIME type of the object **REQUIRED** true **EXAMPLE**
    "application/pdf"
    """

    key: str
    """
    **DESCRIPTION** Object key/path in the bucket **REQUIRED** true **EXAMPLE**
    "my-key"
    """

    module_id: str
    """
    **DESCRIPTION** Module ID identifying the bucket **REQUIRED** true **EXAMPLE**
    "01jtgtrd37acrqf7k24dggg31s"
    """

    organization_id: str
    """**DESCRIPTION** Organization ID for access control **REQUIRED** true"""

    user_id: str
    """**DESCRIPTION** User ID for access control **REQUIRED** true"""
