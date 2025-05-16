# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import summarize_page_create_summary_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.summarize_page_create_summary_response import SummarizePageCreateSummaryResponse

__all__ = ["SummarizePageResource", "AsyncSummarizePageResource"]


class SummarizePageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SummarizePageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/raindrop-python#accessing-raw-response-data-eg-headers
        """
        return SummarizePageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SummarizePageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/raindrop-python#with_streaming_response
        """
        return SummarizePageResourceWithStreamingResponse(self)

    def create_summary(
        self,
        *,
        organization_id: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        request_id: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummarizePageCreateSummaryResponse:
        """
        Generates intelligent summaries of search result pages, helping users quickly
        understand large result sets without reading through every document. The system
        analyzes the content of all results on a given page and generates a detailed
        overview.

        The summary system:

        - Identifies key themes and topics
        - Extracts important findings
        - Highlights document relationships
        - Provides content type distribution
        - Summarizes metadata patterns

        This is particularly valuable when dealing with:

        - Large document collections
        - Mixed content types
        - Technical documentation
        - Research materials

        Args:
          page: **DESCRIPTION** Target page number (1-based) **EXAMPLE** 1 **REQUIRED** TRUE

          page_size: **DESCRIPTION** Results per page. Affects summary granularity **EXAMPLE** 10
              **REQUIRED** TRUE

          request_id: **DESCRIPTION** Original search session identifier from the initial search
              **EXAMPLE** "123e4567-e89b-12d3-a456-426614174000" **REQUIRED** TRUE

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/summarize_page",
            body=maybe_transform(
                {
                    "organization_id": organization_id,
                    "page": page,
                    "page_size": page_size,
                    "request_id": request_id,
                    "user_id": user_id,
                },
                summarize_page_create_summary_params.SummarizePageCreateSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummarizePageCreateSummaryResponse,
        )


class AsyncSummarizePageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSummarizePageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/raindrop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSummarizePageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSummarizePageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/raindrop-python#with_streaming_response
        """
        return AsyncSummarizePageResourceWithStreamingResponse(self)

    async def create_summary(
        self,
        *,
        organization_id: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        request_id: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummarizePageCreateSummaryResponse:
        """
        Generates intelligent summaries of search result pages, helping users quickly
        understand large result sets without reading through every document. The system
        analyzes the content of all results on a given page and generates a detailed
        overview.

        The summary system:

        - Identifies key themes and topics
        - Extracts important findings
        - Highlights document relationships
        - Provides content type distribution
        - Summarizes metadata patterns

        This is particularly valuable when dealing with:

        - Large document collections
        - Mixed content types
        - Technical documentation
        - Research materials

        Args:
          page: **DESCRIPTION** Target page number (1-based) **EXAMPLE** 1 **REQUIRED** TRUE

          page_size: **DESCRIPTION** Results per page. Affects summary granularity **EXAMPLE** 10
              **REQUIRED** TRUE

          request_id: **DESCRIPTION** Original search session identifier from the initial search
              **EXAMPLE** "123e4567-e89b-12d3-a456-426614174000" **REQUIRED** TRUE

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/summarize_page",
            body=await async_maybe_transform(
                {
                    "organization_id": organization_id,
                    "page": page,
                    "page_size": page_size,
                    "request_id": request_id,
                    "user_id": user_id,
                },
                summarize_page_create_summary_params.SummarizePageCreateSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummarizePageCreateSummaryResponse,
        )


class SummarizePageResourceWithRawResponse:
    def __init__(self, summarize_page: SummarizePageResource) -> None:
        self._summarize_page = summarize_page

        self.create_summary = to_raw_response_wrapper(
            summarize_page.create_summary,
        )


class AsyncSummarizePageResourceWithRawResponse:
    def __init__(self, summarize_page: AsyncSummarizePageResource) -> None:
        self._summarize_page = summarize_page

        self.create_summary = async_to_raw_response_wrapper(
            summarize_page.create_summary,
        )


class SummarizePageResourceWithStreamingResponse:
    def __init__(self, summarize_page: SummarizePageResource) -> None:
        self._summarize_page = summarize_page

        self.create_summary = to_streamed_response_wrapper(
            summarize_page.create_summary,
        )


class AsyncSummarizePageResourceWithStreamingResponse:
    def __init__(self, summarize_page: AsyncSummarizePageResource) -> None:
        self._summarize_page = summarize_page

        self.create_summary = async_to_streamed_response_wrapper(
            summarize_page.create_summary,
        )
