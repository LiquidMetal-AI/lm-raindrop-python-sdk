# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.storage_object_delete_response import StorageObjectDeleteResponse

__all__ = ["StorageObjectResource", "AsyncStorageObjectResource"]


class StorageObjectResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StorageObjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/LiquidMetal-AI/lm-raindrop-python-sdk#accessing-raw-response-data-eg-headers
        """
        return StorageObjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StorageObjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/LiquidMetal-AI/lm-raindrop-python-sdk#with_streaming_response
        """
        return StorageObjectResourceWithStreamingResponse(self)

    def delete(
        self,
        key: str,
        *,
        bucket: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StorageObjectDeleteResponse:
        """Delete a file from a SmartBucket or regular bucket.

        The bucket parameter (ID) is
        used to identify the bucket to delete from. The key is the path to the object in
        the bucket.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket:
            raise ValueError(f"Expected a non-empty value for `bucket` but received {bucket!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._delete(
            f"/v1/object/{bucket}/{key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StorageObjectDeleteResponse,
        )


class AsyncStorageObjectResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStorageObjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/LiquidMetal-AI/lm-raindrop-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncStorageObjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStorageObjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/LiquidMetal-AI/lm-raindrop-python-sdk#with_streaming_response
        """
        return AsyncStorageObjectResourceWithStreamingResponse(self)

    async def delete(
        self,
        key: str,
        *,
        bucket: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StorageObjectDeleteResponse:
        """Delete a file from a SmartBucket or regular bucket.

        The bucket parameter (ID) is
        used to identify the bucket to delete from. The key is the path to the object in
        the bucket.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket:
            raise ValueError(f"Expected a non-empty value for `bucket` but received {bucket!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._delete(
            f"/v1/object/{bucket}/{key}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StorageObjectDeleteResponse,
        )


class StorageObjectResourceWithRawResponse:
    def __init__(self, storage_object: StorageObjectResource) -> None:
        self._storage_object = storage_object

        self.delete = to_raw_response_wrapper(
            storage_object.delete,
        )


class AsyncStorageObjectResourceWithRawResponse:
    def __init__(self, storage_object: AsyncStorageObjectResource) -> None:
        self._storage_object = storage_object

        self.delete = async_to_raw_response_wrapper(
            storage_object.delete,
        )


class StorageObjectResourceWithStreamingResponse:
    def __init__(self, storage_object: StorageObjectResource) -> None:
        self._storage_object = storage_object

        self.delete = to_streamed_response_wrapper(
            storage_object.delete,
        )


class AsyncStorageObjectResourceWithStreamingResponse:
    def __init__(self, storage_object: AsyncStorageObjectResource) -> None:
        self._storage_object = storage_object

        self.delete = async_to_streamed_response_wrapper(
            storage_object.delete,
        )
