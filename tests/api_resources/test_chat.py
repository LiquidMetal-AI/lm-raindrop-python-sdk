# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lm_raindrop import Raindrop, AsyncRaindrop
from tests.utils import assert_matches_type
from lm_raindrop.types import ChatInteractResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_interact(self, client: Raindrop) -> None:
        chat = client.chat.interact(
            bucket_location={"bucket": {}},
            input="What are the key points in this document?",
            object_id="document.pdf",
            request_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(ChatInteractResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_interact(self, client: Raindrop) -> None:
        response = client.chat.with_raw_response.interact(
            bucket_location={"bucket": {}},
            input="What are the key points in this document?",
            object_id="document.pdf",
            request_id="123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatInteractResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_interact(self, client: Raindrop) -> None:
        with client.chat.with_streaming_response.interact(
            bucket_location={"bucket": {}},
            input="What are the key points in this document?",
            object_id="document.pdf",
            request_id="123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatInteractResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_interact(self, async_client: AsyncRaindrop) -> None:
        chat = await async_client.chat.interact(
            bucket_location={"bucket": {}},
            input="What are the key points in this document?",
            object_id="document.pdf",
            request_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(ChatInteractResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_interact(self, async_client: AsyncRaindrop) -> None:
        response = await async_client.chat.with_raw_response.interact(
            bucket_location={"bucket": {}},
            input="What are the key points in this document?",
            object_id="document.pdf",
            request_id="123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatInteractResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_interact(self, async_client: AsyncRaindrop) -> None:
        async with async_client.chat.with_streaming_response.interact(
            bucket_location={"bucket": {}},
            input="What are the key points in this document?",
            object_id="document.pdf",
            request_id="123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatInteractResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
