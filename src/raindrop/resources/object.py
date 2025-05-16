# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

import httpx

from ..types import object_list_params, object_upload_params, object_retrieve_params
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
from ..types.object_list_response import ObjectListResponse
from ..types.object_upload_response import ObjectUploadResponse
from ..types.object_retrieve_response import ObjectRetrieveResponse

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

    def retrieve(
        self,
        object_key: str,
        *,
        bucket_name: str,
        key: str | NotGiven = NOT_GIVEN,
        module_id: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectRetrieveResponse:
        """**DESCRIPTION** Delete a file from a SmartBucket or regular bucket.

        The bucket
        parameter (ID) is used to identify the bucket to delete from. The key is the
        path to the object in the bucket.

        Args:
          bucket_name: **DESCRIPTION** Name of the bucket **REQUIRED** true

          object_key: **DESCRIPTION** Key/path of the object in the bucket **REQUIRED** true

          key: **DESCRIPTION** Object key/path to delete **REQUIRED** true **EXAMPLE** "my-key"

          module_id: **DESCRIPTION** Module ID identifying the bucket **REQUIRED** true **EXAMPLE**
              "01jtgtrd37acrqf7k24dggg31s"

          organization_id: **DESCRIPTION** Organization ID for access control **REQUIRED** true

          user_id: **DESCRIPTION** User ID for access control **REQUIRED** true

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
                        "organization_id": organization_id,
                        "user_id": user_id,
                    },
                    object_retrieve_params.ObjectRetrieveParams,
                ),
            ),
            cast_to=ObjectRetrieveResponse,
        )

    def list(
        self,
        bucket_name: str,
        *,
        module_id: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectListResponse:
        """**DESCRIPTION** List all objects in a SmartBucket or regular bucket.

        The bucket
        parameter (ID) is used to identify the bucket to list objects from.

        Args:
          bucket_name: **DESCRIPTION** Name of the bucket **REQUIRED** true

          module_id: **DESCRIPTION** Module ID identifying the bucket **REQUIRED** true **EXAMPLE**
              "01jtgtrd37acrqf7k24dggg31s"

          organization_id: **DESCRIPTION** Organization ID for access control **REQUIRED** true

          user_id: **DESCRIPTION** User ID for access control **REQUIRED** true

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
                query=maybe_transform(
                    {
                        "module_id": module_id,
                        "organization_id": organization_id,
                        "user_id": user_id,
                    },
                    object_list_params.ObjectListParams,
                ),
            ),
            cast_to=ObjectListResponse,
        )

    def upload(
        self,
        path_object_key: str,
        *,
        path_bucket_name: str,
        body_bucket_name: str | NotGiven = NOT_GIVEN,
        content: Union[str, Base64FileInput] | NotGiven = NOT_GIVEN,
        content_type: str | NotGiven = NOT_GIVEN,
        key: str | NotGiven = NOT_GIVEN,
        module_id: str | NotGiven = NOT_GIVEN,
        body_object_key: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectUploadResponse:
        """
        PutObject uploads an object to a bucket **DESCRIPTION** Upload a file to a
        SmartBucket or regular bucket. The bucket parameter (ID) is used to identify the
        bucket to upload to. The key is the path to the object in the bucket.

        Args:
          path_bucket_name: **DESCRIPTION** Name of the bucket **REQUIRED** true

          path_object_key: **DESCRIPTION** Key/path of the object in the bucket **REQUIRED** true

          body_bucket_name: **DESCRIPTION** Name of the bucket **REQUIRED** true

          content: **DESCRIPTION** Binary content of the object **REQUIRED** true

          content_type: **DESCRIPTION** MIME type of the object **REQUIRED** true **EXAMPLE**
              "application/pdf"

          key: **DESCRIPTION** Object key/path in the bucket **REQUIRED** true **EXAMPLE**
              "my-key"

          module_id: **DESCRIPTION** Module ID identifying the bucket **REQUIRED** true **EXAMPLE**
              "01jtgtrd37acrqf7k24dggg31s"

          body_object_key: **DESCRIPTION** Key/path of the object in the bucket **REQUIRED** true

          organization_id: **DESCRIPTION** Organization ID for access control **REQUIRED** true

          user_id: **DESCRIPTION** User ID for access control **REQUIRED** true

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_bucket_name:
            raise ValueError(f"Expected a non-empty value for `path_bucket_name` but received {path_bucket_name!r}")
        if not path_object_key:
            raise ValueError(f"Expected a non-empty value for `path_object_key` but received {path_object_key!r}")
        return self._post(
            f"/v1/object/{path_bucket_name}/{path_object_key}",
            body=maybe_transform(
                {
                    "body_bucket_name": body_bucket_name,
                    "content": content,
                    "content_type": content_type,
                    "key": key,
                    "module_id": module_id,
                    "body_object_key": body_object_key,
                    "organization_id": organization_id,
                    "user_id": user_id,
                },
                object_upload_params.ObjectUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectUploadResponse,
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

    async def retrieve(
        self,
        object_key: str,
        *,
        bucket_name: str,
        key: str | NotGiven = NOT_GIVEN,
        module_id: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectRetrieveResponse:
        """**DESCRIPTION** Delete a file from a SmartBucket or regular bucket.

        The bucket
        parameter (ID) is used to identify the bucket to delete from. The key is the
        path to the object in the bucket.

        Args:
          bucket_name: **DESCRIPTION** Name of the bucket **REQUIRED** true

          object_key: **DESCRIPTION** Key/path of the object in the bucket **REQUIRED** true

          key: **DESCRIPTION** Object key/path to delete **REQUIRED** true **EXAMPLE** "my-key"

          module_id: **DESCRIPTION** Module ID identifying the bucket **REQUIRED** true **EXAMPLE**
              "01jtgtrd37acrqf7k24dggg31s"

          organization_id: **DESCRIPTION** Organization ID for access control **REQUIRED** true

          user_id: **DESCRIPTION** User ID for access control **REQUIRED** true

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
                        "organization_id": organization_id,
                        "user_id": user_id,
                    },
                    object_retrieve_params.ObjectRetrieveParams,
                ),
            ),
            cast_to=ObjectRetrieveResponse,
        )

    async def list(
        self,
        bucket_name: str,
        *,
        module_id: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectListResponse:
        """**DESCRIPTION** List all objects in a SmartBucket or regular bucket.

        The bucket
        parameter (ID) is used to identify the bucket to list objects from.

        Args:
          bucket_name: **DESCRIPTION** Name of the bucket **REQUIRED** true

          module_id: **DESCRIPTION** Module ID identifying the bucket **REQUIRED** true **EXAMPLE**
              "01jtgtrd37acrqf7k24dggg31s"

          organization_id: **DESCRIPTION** Organization ID for access control **REQUIRED** true

          user_id: **DESCRIPTION** User ID for access control **REQUIRED** true

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
                    {
                        "module_id": module_id,
                        "organization_id": organization_id,
                        "user_id": user_id,
                    },
                    object_list_params.ObjectListParams,
                ),
            ),
            cast_to=ObjectListResponse,
        )

    async def upload(
        self,
        path_object_key: str,
        *,
        path_bucket_name: str,
        body_bucket_name: str | NotGiven = NOT_GIVEN,
        content: Union[str, Base64FileInput] | NotGiven = NOT_GIVEN,
        content_type: str | NotGiven = NOT_GIVEN,
        key: str | NotGiven = NOT_GIVEN,
        module_id: str | NotGiven = NOT_GIVEN,
        body_object_key: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ObjectUploadResponse:
        """
        PutObject uploads an object to a bucket **DESCRIPTION** Upload a file to a
        SmartBucket or regular bucket. The bucket parameter (ID) is used to identify the
        bucket to upload to. The key is the path to the object in the bucket.

        Args:
          path_bucket_name: **DESCRIPTION** Name of the bucket **REQUIRED** true

          path_object_key: **DESCRIPTION** Key/path of the object in the bucket **REQUIRED** true

          body_bucket_name: **DESCRIPTION** Name of the bucket **REQUIRED** true

          content: **DESCRIPTION** Binary content of the object **REQUIRED** true

          content_type: **DESCRIPTION** MIME type of the object **REQUIRED** true **EXAMPLE**
              "application/pdf"

          key: **DESCRIPTION** Object key/path in the bucket **REQUIRED** true **EXAMPLE**
              "my-key"

          module_id: **DESCRIPTION** Module ID identifying the bucket **REQUIRED** true **EXAMPLE**
              "01jtgtrd37acrqf7k24dggg31s"

          body_object_key: **DESCRIPTION** Key/path of the object in the bucket **REQUIRED** true

          organization_id: **DESCRIPTION** Organization ID for access control **REQUIRED** true

          user_id: **DESCRIPTION** User ID for access control **REQUIRED** true

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_bucket_name:
            raise ValueError(f"Expected a non-empty value for `path_bucket_name` but received {path_bucket_name!r}")
        if not path_object_key:
            raise ValueError(f"Expected a non-empty value for `path_object_key` but received {path_object_key!r}")
        return await self._post(
            f"/v1/object/{path_bucket_name}/{path_object_key}",
            body=await async_maybe_transform(
                {
                    "body_bucket_name": body_bucket_name,
                    "content": content,
                    "content_type": content_type,
                    "key": key,
                    "module_id": module_id,
                    "body_object_key": body_object_key,
                    "organization_id": organization_id,
                    "user_id": user_id,
                },
                object_upload_params.ObjectUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ObjectUploadResponse,
        )


class ObjectResourceWithRawResponse:
    def __init__(self, object: ObjectResource) -> None:
        self._object = object

        self.retrieve = to_raw_response_wrapper(
            object.retrieve,
        )
        self.list = to_raw_response_wrapper(
            object.list,
        )
        self.upload = to_raw_response_wrapper(
            object.upload,
        )


class AsyncObjectResourceWithRawResponse:
    def __init__(self, object: AsyncObjectResource) -> None:
        self._object = object

        self.retrieve = async_to_raw_response_wrapper(
            object.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            object.list,
        )
        self.upload = async_to_raw_response_wrapper(
            object.upload,
        )


class ObjectResourceWithStreamingResponse:
    def __init__(self, object: ObjectResource) -> None:
        self._object = object

        self.retrieve = to_streamed_response_wrapper(
            object.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            object.list,
        )
        self.upload = to_streamed_response_wrapper(
            object.upload,
        )


class AsyncObjectResourceWithStreamingResponse:
    def __init__(self, object: AsyncObjectResource) -> None:
        self._object = object

        self.retrieve = async_to_streamed_response_wrapper(
            object.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            object.list,
        )
        self.upload = async_to_streamed_response_wrapper(
            object.upload,
        )
