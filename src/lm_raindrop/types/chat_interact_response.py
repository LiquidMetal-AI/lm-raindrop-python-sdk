# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ChatInteractResponse"]


class ChatInteractResponse(BaseModel):
    answer: Optional[str] = None
    """
    AI-generated response that may include direct document quotes, content
    summaries, contextual explanations, references to specific sections, and related
    content suggestions
    """
