# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SummarizePageCreateSummaryParams"]


class SummarizePageCreateSummaryParams(TypedDict, total=False):
    organization_id: str

    page: int
    """**DESCRIPTION** Target page number (1-based) **EXAMPLE** 1 **REQUIRED** TRUE"""

    page_size: int
    """**DESCRIPTION** Results per page.

    Affects summary granularity **EXAMPLE** 10 **REQUIRED** TRUE
    """

    request_id: str
    """
    **DESCRIPTION** Original search session identifier from the initial search
    **EXAMPLE** "123e4567-e89b-12d3-a456-426614174000" **REQUIRED** TRUE
    """

    user_id: str
