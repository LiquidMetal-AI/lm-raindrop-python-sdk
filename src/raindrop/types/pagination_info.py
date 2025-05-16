# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PaginationInfo"]


class PaginationInfo(BaseModel):
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
