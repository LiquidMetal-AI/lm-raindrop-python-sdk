# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import liquidmetal_v1alpha1_search_agent_service_get_paginated_results_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import is_given, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.liquidmetal_v1alpha1_search_agent_service_get_paginated_results_response import (
    LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsResponse,
)

__all__ = ["LiquidmetalV1alpha1SearchAgentServiceResource", "AsyncLiquidmetalV1alpha1SearchAgentServiceResource"]


class LiquidmetalV1alpha1SearchAgentServiceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LiquidmetalV1alpha1SearchAgentServiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/raindrop-python#accessing-raw-response-data-eg-headers
        """
        return LiquidmetalV1alpha1SearchAgentServiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LiquidmetalV1alpha1SearchAgentServiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/raindrop-python#with_streaming_response
        """
        return LiquidmetalV1alpha1SearchAgentServiceResourceWithStreamingResponse(self)

    def get_paginated_results(
        self,
        *,
        connect_protocol_version: Literal[1],
        organization_id: str | NotGiven = NOT_GIVEN,
        page: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: Optional[int] | NotGiven = NOT_GIVEN,
        request_id: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsResponse:
        """Retrieve additional pages from a previous search.

        This endpoint enables
        navigation through large result sets while maintaining search context and result
        relevance. Retrieving paginated results requires a valid request_id from a
        previously completed search.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          page: **DESCRIPTION** Requested page number **EXAMPLE** 2 **REQUIRED** TRUE

          page_size: **DESCRIPTION** Results per page **EXAMPLE** 10 **REQUIRED** TRUE

          request_id: **DESCRIPTION** Original search session identifier from the initial search
              **EXAMPLE** "123e4567-e89b-12d3-a456-426614174000" **REQUIRED** TRUE

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Connect-Protocol-Version": str(connect_protocol_version),
                    "Connect-Timeout-Ms": str(connect_timeout_ms) if is_given(connect_timeout_ms) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/liquidmetal.v1alpha1.SearchAgentService/GetPaginatedResults",
            body=maybe_transform(
                {
                    "organization_id": organization_id,
                    "page": page,
                    "page_size": page_size,
                    "request_id": request_id,
                    "user_id": user_id,
                },
                liquidmetal_v1alpha1_search_agent_service_get_paginated_results_params.LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsResponse,
        )


class AsyncLiquidmetalV1alpha1SearchAgentServiceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLiquidmetalV1alpha1SearchAgentServiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/raindrop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLiquidmetalV1alpha1SearchAgentServiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLiquidmetalV1alpha1SearchAgentServiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/raindrop-python#with_streaming_response
        """
        return AsyncLiquidmetalV1alpha1SearchAgentServiceResourceWithStreamingResponse(self)

    async def get_paginated_results(
        self,
        *,
        connect_protocol_version: Literal[1],
        organization_id: str | NotGiven = NOT_GIVEN,
        page: Optional[int] | NotGiven = NOT_GIVEN,
        page_size: Optional[int] | NotGiven = NOT_GIVEN,
        request_id: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsResponse:
        """Retrieve additional pages from a previous search.

        This endpoint enables
        navigation through large result sets while maintaining search context and result
        relevance. Retrieving paginated results requires a valid request_id from a
        previously completed search.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          page: **DESCRIPTION** Requested page number **EXAMPLE** 2 **REQUIRED** TRUE

          page_size: **DESCRIPTION** Results per page **EXAMPLE** 10 **REQUIRED** TRUE

          request_id: **DESCRIPTION** Original search session identifier from the initial search
              **EXAMPLE** "123e4567-e89b-12d3-a456-426614174000" **REQUIRED** TRUE

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Connect-Protocol-Version": str(connect_protocol_version),
                    "Connect-Timeout-Ms": str(connect_timeout_ms) if is_given(connect_timeout_ms) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/liquidmetal.v1alpha1.SearchAgentService/GetPaginatedResults",
            body=await async_maybe_transform(
                {
                    "organization_id": organization_id,
                    "page": page,
                    "page_size": page_size,
                    "request_id": request_id,
                    "user_id": user_id,
                },
                liquidmetal_v1alpha1_search_agent_service_get_paginated_results_params.LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsResponse,
        )


class LiquidmetalV1alpha1SearchAgentServiceResourceWithRawResponse:
    def __init__(
        self, liquidmetal_v1alpha1_search_agent_service: LiquidmetalV1alpha1SearchAgentServiceResource
    ) -> None:
        self._liquidmetal_v1alpha1_search_agent_service = liquidmetal_v1alpha1_search_agent_service

        self.get_paginated_results = to_raw_response_wrapper(
            liquidmetal_v1alpha1_search_agent_service.get_paginated_results,
        )


class AsyncLiquidmetalV1alpha1SearchAgentServiceResourceWithRawResponse:
    def __init__(
        self, liquidmetal_v1alpha1_search_agent_service: AsyncLiquidmetalV1alpha1SearchAgentServiceResource
    ) -> None:
        self._liquidmetal_v1alpha1_search_agent_service = liquidmetal_v1alpha1_search_agent_service

        self.get_paginated_results = async_to_raw_response_wrapper(
            liquidmetal_v1alpha1_search_agent_service.get_paginated_results,
        )


class LiquidmetalV1alpha1SearchAgentServiceResourceWithStreamingResponse:
    def __init__(
        self, liquidmetal_v1alpha1_search_agent_service: LiquidmetalV1alpha1SearchAgentServiceResource
    ) -> None:
        self._liquidmetal_v1alpha1_search_agent_service = liquidmetal_v1alpha1_search_agent_service

        self.get_paginated_results = to_streamed_response_wrapper(
            liquidmetal_v1alpha1_search_agent_service.get_paginated_results,
        )


class AsyncLiquidmetalV1alpha1SearchAgentServiceResourceWithStreamingResponse:
    def __init__(
        self, liquidmetal_v1alpha1_search_agent_service: AsyncLiquidmetalV1alpha1SearchAgentServiceResource
    ) -> None:
        self._liquidmetal_v1alpha1_search_agent_service = liquidmetal_v1alpha1_search_agent_service

        self.get_paginated_results = async_to_streamed_response_wrapper(
            liquidmetal_v1alpha1_search_agent_service.get_paginated_results,
        )
