# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "DocumentQueryAskParams",
    "BucketLocation",
    "BucketLocationModuleID",
    "BucketLocationBucket",
    "BucketLocationBucketBucket",
]


class DocumentQueryAskParams(TypedDict, total=False):
    bucket_location: Required[BucketLocation]
    """The storage bucket location containing the target document.

    Can specify either module_id (version-agnostic) or specific bucket details
    """

    input: Required[str]
    """User's input or question about the document.

    Can be natural language questions, commands, or requests
    """

    object_id: Required[str]
    """Document identifier within the bucket.

    Typically matches the storage path or key
    """

    request_id: Required[str]
    """Client-provided conversation session identifier.

    Required for maintaining context in follow-up questions. We recommend using a
    UUID or ULID for this value.
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
