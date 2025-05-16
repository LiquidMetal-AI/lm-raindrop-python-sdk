# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StorageObjectRetrieveObjectParams"]


class StorageObjectRetrieveObjectParams(TypedDict, total=False):
    bucket_name: Required[str]

    key: str
    """Object key/path to delete"""

    module_id: str
    """Module ID identifying the bucket"""
