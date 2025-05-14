# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["SearchFindParams", "BucketLocation"]


class SearchFindParams(TypedDict, total=False):
    bucket_locations: Required[Iterable[BucketLocation]]
    """Optional list of specific bucket locations to search in.

    If not provided, searches the latest version of all buckets
    """

    input: Required[str]
    """Natural language search query that can include complex criteria"""

    request_id: Required[str]
    """Client-provided search session identifier.

    Required for pagination and result tracking. We recommend using a UUID or ULID
    for this value.
    """


class BucketLocation(TypedDict, total=False):
    smartbucket_id: Required[str]
    """Identifier for the smartbucket (moduleId)"""
