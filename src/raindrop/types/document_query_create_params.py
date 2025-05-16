# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .bucket_locator_param import BucketLocatorParam

__all__ = ["DocumentQueryCreateParams"]


class DocumentQueryCreateParams(TypedDict, total=False):
    bucket_location: BucketLocatorParam
    """**DESCRIPTION** The storage bucket containing the target document.

    Must be a valid, registered Smart Bucket. Used to identify which bucket to query
    against **EXAMPLE** {"bucket": {"name": "my-bucket", "version":
    "01jtgtraw3b5qbahrhvrj3ygbb", "application_name": "my-app"}} **REQUIRED** TRUE
    """

    input: str
    """**DESCRIPTION** User's input or question about the document.

    Can be natural language questions, commands, or requests. The system will
    process this against the document content **EXAMPLE** "What are the key points
    in this document?" **REQUIRED** TRUE
    """

    object_id: str
    """**DESCRIPTION** Document identifier within the bucket.

    Typically matches the storage path or key. Used to identify which document to
    chat with **EXAMPLE** "document.pdf" **REQUIRED** TRUE
    """

    organization_id: str

    request_id: str
    """**DESCRIPTION** Client-provided conversation session identifier.

    Required for maintaining context in follow-up questions. We recommend using a
    UUID or ULID for this value **EXAMPLE** "123e4567-e89b-12d3-a456-426614174000"
    **REQUIRED** TRUE
    """

    user_id: str
