# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ObjectListParams"]


class ObjectListParams(TypedDict, total=False):
    module_id: str
    """
    **DESCRIPTION** Module ID identifying the bucket **REQUIRED** true **EXAMPLE**
    "01jtgtrd37acrqf7k24dggg31s"
    """

    organization_id: str
    """**DESCRIPTION** Organization ID for access control **REQUIRED** true"""

    user_id: str
    """**DESCRIPTION** User ID for access control **REQUIRED** true"""
