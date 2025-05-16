# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .bucket_locator_param import BucketLocatorParam

__all__ = ["SearchRunParams"]


class SearchRunParams(TypedDict, total=False):
    bucket_locations: Iterable[BucketLocatorParam]
    """**DESCRIPTION** The buckets to search.

    If provided, the search will only return results from these buckets **EXAMPLE**
    [{"bucket": {"name": "my-bucket", "version": "01jtgtraw3b5qbahrhvrj3ygbb",
    "application_name": "my-app"}}] **REQUIRED** TRUE
    """

    input: str
    """**DESCRIPTION** Natural language search query that can include complex criteria.

    Supports queries like finding documents with specific content types, PII, or
    semantic meaning **EXAMPLE** "Show me documents containing credit card numbers
    or social security numbers" **REQUIRED** TRUE
    """

    organization_id: str

    request_id: str
    """**DESCRIPTION** Client-provided search session identifier.

    Required for pagination and result tracking. We recommend using a UUID or ULID
    for this value **EXAMPLE** "123e4567-e89b-12d3-a456-426614174000" **REQUIRED**
    TRUE
    """

    user_id: str
