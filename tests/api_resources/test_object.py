# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lm_raindrop import Raindrop, AsyncRaindrop
from tests.utils import assert_matches_type
from lm_raindrop.types import (
    ObjectPutObjectResponse,
    ObjectListObjectsResponse,
    ObjectRetrieveObjectResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestObject:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_objects(self, client: Raindrop) -> None:
        object_ = client.object.list_objects(
            bucket_name="bucket_name",
        )
        assert_matches_type(ObjectListObjectsResponse, object_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_objects_with_all_params(self, client: Raindrop) -> None:
        object_ = client.object.list_objects(
            bucket_name="bucket_name",
            module_id="01jtgtrd37acrqf7k24dggg31s",
        )
        assert_matches_type(ObjectListObjectsResponse, object_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_objects(self, client: Raindrop) -> None:
        response = client.object.with_raw_response.list_objects(
            bucket_name="bucket_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ObjectListObjectsResponse, object_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_objects(self, client: Raindrop) -> None:
        with client.object.with_streaming_response.list_objects(
            bucket_name="bucket_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ObjectListObjectsResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_objects(self, client: Raindrop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.object.with_raw_response.list_objects(
                bucket_name="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_put_object(self, client: Raindrop) -> None:
        object_ = client.object.put_object(
            object_key="object_key",
            bucket_name="bucket_name",
        )
        assert_matches_type(ObjectPutObjectResponse, object_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_put_object_with_all_params(self, client: Raindrop) -> None:
        object_ = client.object.put_object(
            object_key="object_key",
            bucket_name="bucket_name",
            content="U3RhaW5sZXNzIHJvY2tz",
            content_type="application/pdf",
            key="my-key",
            module_id="01jtgtrd37acrqf7k24dggg31s",
        )
        assert_matches_type(ObjectPutObjectResponse, object_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_put_object(self, client: Raindrop) -> None:
        response = client.object.with_raw_response.put_object(
            object_key="object_key",
            bucket_name="bucket_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ObjectPutObjectResponse, object_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_put_object(self, client: Raindrop) -> None:
        with client.object.with_streaming_response.put_object(
            object_key="object_key",
            bucket_name="bucket_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ObjectPutObjectResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_put_object(self, client: Raindrop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.object.with_raw_response.put_object(
                object_key="object_key",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_key` but received ''"):
            client.object.with_raw_response.put_object(
                object_key="",
                bucket_name="bucket_name",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_object(self, client: Raindrop) -> None:
        object_ = client.object.retrieve_object(
            object_key="object_key",
            bucket_name="bucket_name",
        )
        assert_matches_type(ObjectRetrieveObjectResponse, object_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_object_with_all_params(self, client: Raindrop) -> None:
        object_ = client.object.retrieve_object(
            object_key="object_key",
            bucket_name="bucket_name",
            key="my-key",
            module_id="01jtgtrd37acrqf7k24dggg31s",
        )
        assert_matches_type(ObjectRetrieveObjectResponse, object_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_object(self, client: Raindrop) -> None:
        response = client.object.with_raw_response.retrieve_object(
            object_key="object_key",
            bucket_name="bucket_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = response.parse()
        assert_matches_type(ObjectRetrieveObjectResponse, object_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_object(self, client: Raindrop) -> None:
        with client.object.with_streaming_response.retrieve_object(
            object_key="object_key",
            bucket_name="bucket_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = response.parse()
            assert_matches_type(ObjectRetrieveObjectResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_object(self, client: Raindrop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.object.with_raw_response.retrieve_object(
                object_key="object_key",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_key` but received ''"):
            client.object.with_raw_response.retrieve_object(
                object_key="",
                bucket_name="bucket_name",
            )


class TestAsyncObject:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_objects(self, async_client: AsyncRaindrop) -> None:
        object_ = await async_client.object.list_objects(
            bucket_name="bucket_name",
        )
        assert_matches_type(ObjectListObjectsResponse, object_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_objects_with_all_params(self, async_client: AsyncRaindrop) -> None:
        object_ = await async_client.object.list_objects(
            bucket_name="bucket_name",
            module_id="01jtgtrd37acrqf7k24dggg31s",
        )
        assert_matches_type(ObjectListObjectsResponse, object_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_objects(self, async_client: AsyncRaindrop) -> None:
        response = await async_client.object.with_raw_response.list_objects(
            bucket_name="bucket_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ObjectListObjectsResponse, object_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_objects(self, async_client: AsyncRaindrop) -> None:
        async with async_client.object.with_streaming_response.list_objects(
            bucket_name="bucket_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ObjectListObjectsResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_objects(self, async_client: AsyncRaindrop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.object.with_raw_response.list_objects(
                bucket_name="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_put_object(self, async_client: AsyncRaindrop) -> None:
        object_ = await async_client.object.put_object(
            object_key="object_key",
            bucket_name="bucket_name",
        )
        assert_matches_type(ObjectPutObjectResponse, object_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_put_object_with_all_params(self, async_client: AsyncRaindrop) -> None:
        object_ = await async_client.object.put_object(
            object_key="object_key",
            bucket_name="bucket_name",
            content="U3RhaW5sZXNzIHJvY2tz",
            content_type="application/pdf",
            key="my-key",
            module_id="01jtgtrd37acrqf7k24dggg31s",
        )
        assert_matches_type(ObjectPutObjectResponse, object_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_put_object(self, async_client: AsyncRaindrop) -> None:
        response = await async_client.object.with_raw_response.put_object(
            object_key="object_key",
            bucket_name="bucket_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ObjectPutObjectResponse, object_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_put_object(self, async_client: AsyncRaindrop) -> None:
        async with async_client.object.with_streaming_response.put_object(
            object_key="object_key",
            bucket_name="bucket_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ObjectPutObjectResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_put_object(self, async_client: AsyncRaindrop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.object.with_raw_response.put_object(
                object_key="object_key",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_key` but received ''"):
            await async_client.object.with_raw_response.put_object(
                object_key="",
                bucket_name="bucket_name",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_object(self, async_client: AsyncRaindrop) -> None:
        object_ = await async_client.object.retrieve_object(
            object_key="object_key",
            bucket_name="bucket_name",
        )
        assert_matches_type(ObjectRetrieveObjectResponse, object_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_object_with_all_params(self, async_client: AsyncRaindrop) -> None:
        object_ = await async_client.object.retrieve_object(
            object_key="object_key",
            bucket_name="bucket_name",
            key="my-key",
            module_id="01jtgtrd37acrqf7k24dggg31s",
        )
        assert_matches_type(ObjectRetrieveObjectResponse, object_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_object(self, async_client: AsyncRaindrop) -> None:
        response = await async_client.object.with_raw_response.retrieve_object(
            object_key="object_key",
            bucket_name="bucket_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        object_ = await response.parse()
        assert_matches_type(ObjectRetrieveObjectResponse, object_, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_object(self, async_client: AsyncRaindrop) -> None:
        async with async_client.object.with_streaming_response.retrieve_object(
            object_key="object_key",
            bucket_name="bucket_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            object_ = await response.parse()
            assert_matches_type(ObjectRetrieveObjectResponse, object_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_object(self, async_client: AsyncRaindrop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.object.with_raw_response.retrieve_object(
                object_key="object_key",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_key` but received ''"):
            await async_client.object.with_raw_response.retrieve_object(
                object_key="",
                bucket_name="bucket_name",
            )
