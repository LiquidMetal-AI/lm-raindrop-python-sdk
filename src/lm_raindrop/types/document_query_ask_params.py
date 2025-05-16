# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "DocumentQueryAskParams",
    "BucketLocation",
    "BucketLocationBucket",
    "BucketLocationBucketBucket",
    "BucketLocationModuleID",
]


class DocumentQueryAskParams(TypedDict, total=False):
    bucket_location: Required[BucketLocation]
    """The storage bucket containing the target document.

    Must be a valid, registered Smart Bucket. Used to identify which bucket to query
    against
    """

    input: Required[str]
    """User's input or question about the document.

    Can be natural language questions, commands, or requests. The system will
    process this against the document content
    """

    object_id: Required[str]
    """Document identifier within the bucket.

    Typically matches the storage path or key. Used to identify which document to
    chat with
    """

    request_id: Required[str]
    """Client-provided conversation session identifier.

    Required for maintaining context in follow-up questions. We recommend using a
    UUID or ULID for this value
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
