# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ChunkSearchFindParams"]


class ChunkSearchFindParams(TypedDict, total=False):
    bucket_locations: Required[Iterable[object]]

    input: Required[str]
    """Natural language query or question.

    Can include complex criteria and relationships
    """

    request_id: Required[str]
    """Client-provided search session identifier.

    We recommend using a UUID or ULID for this value.
    """
