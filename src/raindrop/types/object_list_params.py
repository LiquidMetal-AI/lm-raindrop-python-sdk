# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ObjectListParams"]


class ObjectListParams(TypedDict, total=False):
    module_id: Required[str]
    """
    **DESCRIPTION** Module ID identifying the bucket **REQUIRED** true **EXAMPLE**
    "01jtgtrd37acrqf7k24dggg31s"
    """

    organization_id: Required[str]
    """**DESCRIPTION** Organization ID for access control **REQUIRED** true"""

    user_id: Required[str]
    """**DESCRIPTION** User ID for access control **REQUIRED** true"""
