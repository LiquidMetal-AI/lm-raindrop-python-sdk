# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

import httpx

from ..types import object_put_object_params, object_list_objects_params, object_retrieve_object_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, Base64FileInput
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
from ..types.object_put_object_response import ObjectPutObjectResponse
from ..types.object_list_objects_response import ObjectListObjectsResponse
from ..types.object_retrieve_object_response import ObjectRetrieveObjectResponse

__all__ = ["ObjectResource", "AsyncObjectResource"]


class ObjectResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ObjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/raindrop-python#accessing-raw-response-data-eg-headers
        """
        return ObjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/raindrop-python#with_streaming_response
        """
        return ObjectResourceWithStreamingResponse(self)

    def list_objects(
        self,
        bucket_name: str,
        *,
        module_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectListObjectsResponse:
        """List all objects in a SmartBucket or regular bucket.

        The bucket parameter (ID)
        is used to identify the bucket to list objects from.

        Args:
          module_id: Module ID identifying the bucket

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return self._get(
            f"/v1/object/{bucket_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"module_id": module_id}, object_list_objects_params.ObjectListObjectsParams),
            ),
            cast_to=ObjectListObjectsResponse,
        )

    def put_object(
        self,
        object_key: str,
        *,
        bucket_name: str,
        content: Union[str, Base64FileInput],
        content_type: str | NotGiven = NOT_GIVEN,
        key: str | NotGiven = NOT_GIVEN,
        module_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectPutObjectResponse:
        """Upload a file to a SmartBucket or regular bucket.

        The bucket parameter (ID) is
        used to identify the bucket to upload to. The key is the path to the object in
        the bucket.

        Args:
          content: Binary content of the object

          content_type: MIME type of the object

          key: Object key/path in the bucket

          module_id: Module ID identifying the bucket

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not object_key:
            raise ValueError(f"Expected a non-empty value for `object_key` but received {object_key!r}")
        return self._post(
            f"/v1/object/{bucket_name}/{object_key}",
            body=maybe_transform(
                {
                    "content": content,
                    "content_type": content_type,
                    "key": key,
                    "module_id": module_id,
                },
                object_put_object_params.ObjectPutObjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectPutObjectResponse,
        )

    def retrieve_object(
        self,
        object_key: str,
        *,
        bucket_name: str,
        key: str | NotGiven = NOT_GIVEN,
        module_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectRetrieveObjectResponse:
        """Delete a file from a SmartBucket or regular bucket.

        The bucket parameter (ID) is
        used to identify the bucket to delete from. The key is the path to the object in
        the bucket.

        Args:
          key: Object key/path to delete

          module_id: Module ID identifying the bucket

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not object_key:
            raise ValueError(f"Expected a non-empty value for `object_key` but received {object_key!r}")
        return self._get(
            f"/v1/object/{bucket_name}/{object_key}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "key": key,
                        "module_id": module_id,
                    },
                    object_retrieve_object_params.ObjectRetrieveObjectParams,
                ),
            ),
            cast_to=ObjectRetrieveObjectResponse,
        )


class AsyncObjectResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncObjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/raindrop-python#accessing-raw-response-data-eg-headers
        """
        return AsyncObjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/raindrop-python#with_streaming_response
        """
        return AsyncObjectResourceWithStreamingResponse(self)

    async def list_objects(
        self,
        bucket_name: str,
        *,
        module_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectListObjectsResponse:
        """List all objects in a SmartBucket or regular bucket.

        The bucket parameter (ID)
        is used to identify the bucket to list objects from.

        Args:
          module_id: Module ID identifying the bucket

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        return await self._get(
            f"/v1/object/{bucket_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"module_id": module_id}, object_list_objects_params.ObjectListObjectsParams
                ),
            ),
            cast_to=ObjectListObjectsResponse,
        )

    async def put_object(
        self,
        object_key: str,
        *,
        bucket_name: str,
        content: Union[str, Base64FileInput],
        content_type: str | NotGiven = NOT_GIVEN,
        key: str | NotGiven = NOT_GIVEN,
        module_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectPutObjectResponse:
        """Upload a file to a SmartBucket or regular bucket.

        The bucket parameter (ID) is
        used to identify the bucket to upload to. The key is the path to the object in
        the bucket.

        Args:
          content: Binary content of the object

          content_type: MIME type of the object

          key: Object key/path in the bucket

          module_id: Module ID identifying the bucket

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not object_key:
            raise ValueError(f"Expected a non-empty value for `object_key` but received {object_key!r}")
        return await self._post(
            f"/v1/object/{bucket_name}/{object_key}",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "content_type": content_type,
                    "key": key,
                    "module_id": module_id,
                },
                object_put_object_params.ObjectPutObjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectPutObjectResponse,
        )

    async def retrieve_object(
        self,
        object_key: str,
        *,
        bucket_name: str,
        key: str | NotGiven = NOT_GIVEN,
        module_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectRetrieveObjectResponse:
        """Delete a file from a SmartBucket or regular bucket.

        The bucket parameter (ID) is
        used to identify the bucket to delete from. The key is the path to the object in
        the bucket.

        Args:
          key: Object key/path to delete

          module_id: Module ID identifying the bucket

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bucket_name:
            raise ValueError(f"Expected a non-empty value for `bucket_name` but received {bucket_name!r}")
        if not object_key:
            raise ValueError(f"Expected a non-empty value for `object_key` but received {object_key!r}")
        return await self._get(
            f"/v1/object/{bucket_name}/{object_key}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "key": key,
                        "module_id": module_id,
                    },
                    object_retrieve_object_params.ObjectRetrieveObjectParams,
                ),
            ),
            cast_to=ObjectRetrieveObjectResponse,
        )


class ObjectResourceWithRawResponse:
    def __init__(self, object: ObjectResource) -> None:
        self._object = object

        self.list_objects = to_raw_response_wrapper(
            object.list_objects,
        )
        self.put_object = to_raw_response_wrapper(
            object.put_object,
        )
        self.retrieve_object = to_raw_response_wrapper(
            object.retrieve_object,
        )


class AsyncObjectResourceWithRawResponse:
    def __init__(self, object: AsyncObjectResource) -> None:
        self._object = object

        self.list_objects = async_to_raw_response_wrapper(
            object.list_objects,
        )
        self.put_object = async_to_raw_response_wrapper(
            object.put_object,
        )
        self.retrieve_object = async_to_raw_response_wrapper(
            object.retrieve_object,
        )


class ObjectResourceWithStreamingResponse:
    def __init__(self, object: ObjectResource) -> None:
        self._object = object

        self.list_objects = to_streamed_response_wrapper(
            object.list_objects,
        )
        self.put_object = to_streamed_response_wrapper(
            object.put_object,
        )
        self.retrieve_object = to_streamed_response_wrapper(
            object.retrieve_object,
        )


class AsyncObjectResourceWithStreamingResponse:
    def __init__(self, object: AsyncObjectResource) -> None:
        self._object = object

        self.list_objects = async_to_streamed_response_wrapper(
            object.list_objects,
        )
        self.put_object = async_to_streamed_response_wrapper(
            object.put_object,
        )
        self.retrieve_object = async_to_streamed_response_wrapper(
            object.retrieve_object,
        )
