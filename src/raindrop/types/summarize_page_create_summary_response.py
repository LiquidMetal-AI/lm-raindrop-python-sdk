# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SummarizePageCreateSummaryResponse"]


class SummarizePageCreateSummaryResponse(BaseModel):
    summary: Optional[str] = None
    """
    **DESCRIPTION** AI-generated summary including key themes and topics, content
    type distribution, important findings, and document relationships **EXAMPLE**
    "The search results contain information about..."
    """
