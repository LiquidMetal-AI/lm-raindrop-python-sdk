# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ChunkSearchFindParams", "BucketLocation"]


class ChunkSearchFindParams(TypedDict, total=False):
    input: Required[str]
    """Natural language query or question.

    Can include complex criteria and relationships
    """

    request_id: Required[str]
    """Client-provided search session identifier.

    We recommend using a UUID or ULID for this value.
    """

    bucket_locations: Iterable[BucketLocation]
    """Optional list of specific bucket locations to search in.

    If not provided, searches the latest version of all accessible buckets
    """


class BucketLocation(TypedDict, total=False):
    smartbucket_id: Required[str]
    """Identifier for the smartbucket (moduleId)"""
