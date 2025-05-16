# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import document_query_create_params
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
from ..types.bucket_locator_param import BucketLocatorParam
from ..types.document_query_create_response import DocumentQueryCreateResponse

__all__ = ["DocumentQueryResource", "AsyncDocumentQueryResource"]


class DocumentQueryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocumentQueryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/raindrop-python#accessing-raw-response-data-eg-headers
        """
        return DocumentQueryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentQueryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/raindrop-python#with_streaming_response
        """
        return DocumentQueryResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        bucket_location: BucketLocatorParam | NotGiven = NOT_GIVEN,
        input: str | NotGiven = NOT_GIVEN,
        object_id: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        request_id: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentQueryCreateResponse:
        """
        Enables natural conversational interactions with documents stored in
        SmartBuckets. This endpoint allows users to ask questions, request summaries,
        and explore document content through an intuitive conversational interface. The
        system understands context and can handle complex queries about document
        contents.

        The query system maintains conversation context throught the request_id,
        enabling follow-up questions and deep exploration of document content. It works
        across all supported file types and automatically handles multi-page documents,
        making complex file interaction as simple as having a conversation.

        The system will:

        - Maintain conversation history for context when using the same request_id
        - Process questions against file content
        - Generate contextual, relevant responses

        Document query is supported for all file types, including PDFs, images, and
        audio files.

        Args:
          bucket_location: **DESCRIPTION** The storage bucket containing the target document. Must be a
              valid, registered Smart Bucket. Used to identify which bucket to query against
              **EXAMPLE** {"bucket": {"name": "my-bucket", "version":
              "01jtgtraw3b5qbahrhvrj3ygbb", "application_name": "my-app"}} **REQUIRED** TRUE

          input: **DESCRIPTION** User's input or question about the document. Can be natural
              language questions, commands, or requests. The system will process this against
              the document content **EXAMPLE** "What are the key points in this document?"
              **REQUIRED** TRUE

          object_id: **DESCRIPTION** Document identifier within the bucket. Typically matches the
              storage path or key. Used to identify which document to chat with **EXAMPLE**
              "document.pdf" **REQUIRED** TRUE

          request_id: **DESCRIPTION** Client-provided conversation session identifier. Required for
              maintaining context in follow-up questions. We recommend using a UUID or ULID
              for this value **EXAMPLE** "123e4567-e89b-12d3-a456-426614174000" **REQUIRED**
              TRUE

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/document_query",
            body=maybe_transform(
                {
                    "bucket_location": bucket_location,
                    "input": input,
                    "object_id": object_id,
                    "organization_id": organization_id,
                    "request_id": request_id,
                    "user_id": user_id,
                },
                document_query_create_params.DocumentQueryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentQueryCreateResponse,
        )


class AsyncDocumentQueryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocumentQueryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/raindrop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDocumentQueryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentQueryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/raindrop-python#with_streaming_response
        """
        return AsyncDocumentQueryResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        bucket_location: BucketLocatorParam | NotGiven = NOT_GIVEN,
        input: str | NotGiven = NOT_GIVEN,
        object_id: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        request_id: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentQueryCreateResponse:
        """
        Enables natural conversational interactions with documents stored in
        SmartBuckets. This endpoint allows users to ask questions, request summaries,
        and explore document content through an intuitive conversational interface. The
        system understands context and can handle complex queries about document
        contents.

        The query system maintains conversation context throught the request_id,
        enabling follow-up questions and deep exploration of document content. It works
        across all supported file types and automatically handles multi-page documents,
        making complex file interaction as simple as having a conversation.

        The system will:

        - Maintain conversation history for context when using the same request_id
        - Process questions against file content
        - Generate contextual, relevant responses

        Document query is supported for all file types, including PDFs, images, and
        audio files.

        Args:
          bucket_location: **DESCRIPTION** The storage bucket containing the target document. Must be a
              valid, registered Smart Bucket. Used to identify which bucket to query against
              **EXAMPLE** {"bucket": {"name": "my-bucket", "version":
              "01jtgtraw3b5qbahrhvrj3ygbb", "application_name": "my-app"}} **REQUIRED** TRUE

          input: **DESCRIPTION** User's input or question about the document. Can be natural
              language questions, commands, or requests. The system will process this against
              the document content **EXAMPLE** "What are the key points in this document?"
              **REQUIRED** TRUE

          object_id: **DESCRIPTION** Document identifier within the bucket. Typically matches the
              storage path or key. Used to identify which document to chat with **EXAMPLE**
              "document.pdf" **REQUIRED** TRUE

          request_id: **DESCRIPTION** Client-provided conversation session identifier. Required for
              maintaining context in follow-up questions. We recommend using a UUID or ULID
              for this value **EXAMPLE** "123e4567-e89b-12d3-a456-426614174000" **REQUIRED**
              TRUE

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/document_query",
            body=await async_maybe_transform(
                {
                    "bucket_location": bucket_location,
                    "input": input,
                    "object_id": object_id,
                    "organization_id": organization_id,
                    "request_id": request_id,
                    "user_id": user_id,
                },
                document_query_create_params.DocumentQueryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentQueryCreateResponse,
        )


class DocumentQueryResourceWithRawResponse:
    def __init__(self, document_query: DocumentQueryResource) -> None:
        self._document_query = document_query

        self.create = to_raw_response_wrapper(
            document_query.create,
        )


class AsyncDocumentQueryResourceWithRawResponse:
    def __init__(self, document_query: AsyncDocumentQueryResource) -> None:
        self._document_query = document_query

        self.create = async_to_raw_response_wrapper(
            document_query.create,
        )


class DocumentQueryResourceWithStreamingResponse:
    def __init__(self, document_query: DocumentQueryResource) -> None:
        self._document_query = document_query

        self.create = to_streamed_response_wrapper(
            document_query.create,
        )


class AsyncDocumentQueryResourceWithStreamingResponse:
    def __init__(self, document_query: AsyncDocumentQueryResource) -> None:
        self._document_query = document_query

        self.create = async_to_streamed_response_wrapper(
            document_query.create,
        )
