# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .text_result import TextResult

__all__ = ["SearchRunResponse", "Pagination"]


class Pagination(BaseModel):
    has_more: Optional[bool] = None
    """**DESCRIPTION** Indicates more results available.

    Used for infinite scroll implementation **EXAMPLE** true
    """

    page: Optional[int] = None
    """**DESCRIPTION** Current page number (1-based) **EXAMPLE** 1"""

    page_size: Optional[int] = None
    """**DESCRIPTION** Results per page.

    May be adjusted for performance **EXAMPLE** 15
    """

    total: Optional[int] = None
    """**DESCRIPTION** Total number of available results **EXAMPLE** 1020"""

    total_pages: Optional[int] = None
    """**DESCRIPTION** Total available pages.

    Calculated as ceil(total/page_size) **EXAMPLE** 68
    """


class SearchRunResponse(BaseModel):
    pagination: Optional[Pagination] = None
    """
    **DESCRIPTION** Pagination details for result navigation **EXAMPLE** {"total":
    100, "page": 1, "page_size": 10, "total_pages": 10, "has_more": true}
    """

    results: Optional[List[TextResult]] = None
    """
    **DESCRIPTION** Matched results with metadata **EXAMPLE** [{"chunk_signature":
    "chunk_123abc", "text": "Sample text", "score": 0.95}]
    """
