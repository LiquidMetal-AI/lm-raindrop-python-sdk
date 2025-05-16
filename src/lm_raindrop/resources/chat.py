# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import chat_interact_params
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
from ..types.chat_interact_response import ChatInteractResponse

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/LiquidMetal-AI/lm-raindrop-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/LiquidMetal-AI/lm-raindrop-python-sdk#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    def interact(
        self,
        *,
        bucket_location: chat_interact_params.BucketLocation,
        input: str,
        object_id: str,
        request_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatInteractResponse:
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
          bucket_location: The storage bucket containing the target document. Must be a valid, registered
              Smart Bucket. Used to identify which bucket to query against

          input: User's input or question about the document. Can be natural language questions,
              commands, or requests. The system will process this against the document content

          object_id: Document identifier within the bucket. Typically matches the storage path or
              key. Used to identify which document to chat with

          request_id: Client-provided conversation session identifier. Required for maintaining
              context in follow-up questions. We recommend using a UUID or ULID for this value

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/chat",
            body=maybe_transform(
                {
                    "bucket_location": bucket_location,
                    "input": input,
                    "object_id": object_id,
                    "request_id": request_id,
                },
                chat_interact_params.ChatInteractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatInteractResponse,
        )


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/LiquidMetal-AI/lm-raindrop-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/LiquidMetal-AI/lm-raindrop-python-sdk#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    async def interact(
        self,
        *,
        bucket_location: chat_interact_params.BucketLocation,
        input: str,
        object_id: str,
        request_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatInteractResponse:
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
          bucket_location: The storage bucket containing the target document. Must be a valid, registered
              Smart Bucket. Used to identify which bucket to query against

          input: User's input or question about the document. Can be natural language questions,
              commands, or requests. The system will process this against the document content

          object_id: Document identifier within the bucket. Typically matches the storage path or
              key. Used to identify which document to chat with

          request_id: Client-provided conversation session identifier. Required for maintaining
              context in follow-up questions. We recommend using a UUID or ULID for this value

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/chat",
            body=await async_maybe_transform(
                {
                    "bucket_location": bucket_location,
                    "input": input,
                    "object_id": object_id,
                    "request_id": request_id,
                },
                chat_interact_params.ChatInteractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatInteractResponse,
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.interact = to_raw_response_wrapper(
            chat.interact,
        )


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.interact = async_to_raw_response_wrapper(
            chat.interact,
        )


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.interact = to_streamed_response_wrapper(
            chat.interact,
        )


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.interact = async_to_streamed_response_wrapper(
            chat.interact,
        )
