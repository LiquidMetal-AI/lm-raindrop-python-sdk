# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ObjectRetrieveParams"]


class ObjectRetrieveParams(TypedDict, total=False):
    bucket_name: Required[str]

    key: Required[str]
    """
    **DESCRIPTION** Object key/path to download **REQUIRED** true **EXAMPLE**
    "my-key"
    """

    module_id: Required[str]
    """
    **DESCRIPTION** Module ID identifying the bucket **REQUIRED** true **EXAMPLE**
    "01jtgtrd37acrqf7k24dggg31s"
    """

    organization_id: Required[str]
    """**DESCRIPTION** Organization ID for access control **REQUIRED** true"""

    user_id: Required[str]
    """**DESCRIPTION** User ID for access control **REQUIRED** true"""
