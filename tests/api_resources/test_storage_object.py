# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lm_raindrop import Raindrop, AsyncRaindrop
from tests.utils import assert_matches_type
from lm_raindrop.types import StorageObjectDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStorageObject:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Raindrop) -> None:
        storage_object = client.storage_object.delete(
            key="my-key",
            bucket="01jtgtrd37acrqf7k24dggg31s",
        )
        assert_matches_type(StorageObjectDeleteResponse, storage_object, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Raindrop) -> None:
        response = client.storage_object.with_raw_response.delete(
            key="my-key",
            bucket="01jtgtrd37acrqf7k24dggg31s",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage_object = response.parse()
        assert_matches_type(StorageObjectDeleteResponse, storage_object, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Raindrop) -> None:
        with client.storage_object.with_streaming_response.delete(
            key="my-key",
            bucket="01jtgtrd37acrqf7k24dggg31s",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage_object = response.parse()
            assert_matches_type(StorageObjectDeleteResponse, storage_object, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Raindrop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket` but received ''"):
            client.storage_object.with_raw_response.delete(
                key="my-key",
                bucket="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            client.storage_object.with_raw_response.delete(
                key="",
                bucket="01jtgtrd37acrqf7k24dggg31s",
            )


class TestAsyncStorageObject:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncRaindrop) -> None:
        storage_object = await async_client.storage_object.delete(
            key="my-key",
            bucket="01jtgtrd37acrqf7k24dggg31s",
        )
        assert_matches_type(StorageObjectDeleteResponse, storage_object, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRaindrop) -> None:
        response = await async_client.storage_object.with_raw_response.delete(
            key="my-key",
            bucket="01jtgtrd37acrqf7k24dggg31s",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        storage_object = await response.parse()
        assert_matches_type(StorageObjectDeleteResponse, storage_object, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRaindrop) -> None:
        async with async_client.storage_object.with_streaming_response.delete(
            key="my-key",
            bucket="01jtgtrd37acrqf7k24dggg31s",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            storage_object = await response.parse()
            assert_matches_type(StorageObjectDeleteResponse, storage_object, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRaindrop) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket` but received ''"):
            await async_client.storage_object.with_raw_response.delete(
                key="my-key",
                bucket="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key` but received ''"):
            await async_client.storage_object.with_raw_response.delete(
                key="",
                bucket="01jtgtrd37acrqf7k24dggg31s",
            )
