# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "ChunkSearchFindParams",
    "BucketLocation",
    "BucketLocationBucket",
    "BucketLocationBucketBucket",
    "BucketLocationModuleID",
]


class ChunkSearchFindParams(TypedDict, total=False):
    bucket_locations: Required[Iterable[BucketLocation]]
    """The buckets to search.

    If provided, the search will only return results from these buckets
    """

    input: Required[str]
    """Natural language query or question.

    Can include complex criteria and relationships. The system will optimize the
    search strategy based on this input
    """

    request_id: Required[str]
    """Client-provided search session identifier.

    Required for pagination and result tracking. We recommend using a UUID or ULID
    for this value
    """


class BucketLocationBucketBucket(TypedDict, total=False):
    application_name: Optional[str]
    """Optional Application"""

    name: str
    """The name of the bucket"""

    version: Optional[str]
    """Optional version of the bucket"""


class BucketLocationBucket(TypedDict, total=False):
    bucket: Required[BucketLocationBucketBucket]
    """BucketName represents a bucket name with an optional version"""


class BucketLocationModuleID(TypedDict, total=False):
    module_id: Required[str]


BucketLocation: TypeAlias = Union[BucketLocationBucket, BucketLocationModuleID]
