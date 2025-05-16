# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .text_result import TextResult
from .pagination_info import PaginationInfo

__all__ = ["LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsResponse"]


class LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsResponse(BaseModel):
    pagination: Optional[PaginationInfo] = None
    """
    **DESCRIPTION** Updated pagination information **EXAMPLE** {"total": 100,
    "page": 2, "page_size": 10, "total_pages": 10, "has_more": true}
    """

    results: Optional[List[TextResult]] = None
    """
    **DESCRIPTION** Page results with full metadata **EXAMPLE** [{"chunk_signature":
    "chunk_123abc", "text": "Sample text", "score": 0.95}]
    """
