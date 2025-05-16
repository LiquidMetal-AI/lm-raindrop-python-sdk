# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypedDict

from .._types import Base64FileInput
from .._utils import PropertyInfo

__all__ = ["ObjectUploadParams"]


class ObjectUploadParams(TypedDict, total=False):
    bucket_name: Required[str]

    query_key: Required[Annotated[str, PropertyInfo(alias="key")]]
    """
    **DESCRIPTION** Object key/path in the bucket **REQUIRED** true **EXAMPLE**
    "my-key"
    """

    query_module_id: Required[Annotated[str, PropertyInfo(alias="module_id")]]
    """
    **DESCRIPTION** Module ID identifying the bucket **REQUIRED** true **EXAMPLE**
    "01jtgtrd37acrqf7k24dggg31s"
    """

    query_organization_id: Required[Annotated[str, PropertyInfo(alias="organization_id")]]
    """**DESCRIPTION** Organization ID for access control **REQUIRED** true"""

    query_user_id: Required[Annotated[str, PropertyInfo(alias="user_id")]]
    """**DESCRIPTION** User ID for access control **REQUIRED** true"""

    content: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """**DESCRIPTION** Binary content of the object **REQUIRED** true"""

    content_type: str
    """
    **DESCRIPTION** MIME type of the object **REQUIRED** true **EXAMPLE**
    "application/pdf"
    """

    body_key: Annotated[str, PropertyInfo(alias="key")]
    """
    **DESCRIPTION** Object key/path in the bucket **REQUIRED** true **EXAMPLE**
    "my-key"
    """

    body_module_id: Annotated[str, PropertyInfo(alias="module_id")]
    """
    **DESCRIPTION** Module ID identifying the bucket **REQUIRED** true **EXAMPLE**
    "01jtgtrd37acrqf7k24dggg31s"
    """

    body_organization_id: Annotated[str, PropertyInfo(alias="organization_id")]
    """**DESCRIPTION** Organization ID for access control **REQUIRED** true"""

    body_user_id: Annotated[str, PropertyInfo(alias="user_id")]
    """**DESCRIPTION** User ID for access control **REQUIRED** true"""
