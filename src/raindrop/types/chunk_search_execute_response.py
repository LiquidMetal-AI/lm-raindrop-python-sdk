# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .text_result import TextResult

__all__ = ["ChunkSearchExecuteResponse"]


class ChunkSearchExecuteResponse(BaseModel):
    results: Optional[List[TextResult]] = None
    """**DESCRIPTION** Ordered list of relevant text segments.

    Each result includes full context and metadata **EXAMPLE** [{"chunk_signature":
    "chunk_123abc", "text": "Sample text", "score": 0.95}]
    """
