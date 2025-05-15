# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "SearchFindParams",
    "BucketLocation",
    "BucketLocationModuleID",
    "BucketLocationBucket",
    "BucketLocationBucketBucket",
]


class SearchFindParams(TypedDict, total=False):
    bucket_locations: Required[Iterable[BucketLocation]]

    input: Required[str]
    """Natural language search query that can include complex criteria"""

    request_id: Required[str]
    """Client-provided search session identifier.

    Required for pagination and result tracking. We recommend using a UUID or ULID
    for this value.
    """


class BucketLocationModuleID(TypedDict, total=False):
    module_id: Required[str]
    """Version-agnostic identifier for a module"""


class BucketLocationBucketBucket(TypedDict, total=False):
    application_name: Required[str]
    """Name of the application"""

    name: Required[str]
    """Name of the bucket"""

    version: Required[str]
    """Version of the bucket"""


class BucketLocationBucket(TypedDict, total=False):
    bucket: Required[BucketLocationBucketBucket]


BucketLocation: TypeAlias = Union[BucketLocationModuleID, BucketLocationBucket]
