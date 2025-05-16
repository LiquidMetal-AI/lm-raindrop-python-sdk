# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsParams"]


class LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsParams(TypedDict, total=False):
    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    organization_id: str

    page: Optional[int]
    """**DESCRIPTION** Requested page number **EXAMPLE** 2 **REQUIRED** TRUE"""

    page_size: Optional[int]
    """**DESCRIPTION** Results per page **EXAMPLE** 10 **REQUIRED** TRUE"""

    request_id: str
    """
    **DESCRIPTION** Original search session identifier from the initial search
    **EXAMPLE** "123e4567-e89b-12d3-a456-426614174000" **REQUIRED** TRUE
    """

    user_id: str

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""
