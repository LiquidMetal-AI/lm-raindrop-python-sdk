# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SummarizePageCreateParams"]


class SummarizePageCreateParams(TypedDict, total=False):
    page: int
    """Target page number (1-based)"""

    page_size: int
    """Results per page. Affects summary granularity"""

    request_id: str
    """Original search session identifier from the initial search"""
