# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from raindrop import Raindrop, AsyncRaindrop
from tests.utils import assert_matches_type
from raindrop.types import (
    LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLiquidmetalV1alpha1SearchAgentService:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_paginated_results(self, client: Raindrop) -> None:
        liquidmetal_v1alpha1_search_agent_service = (
            client.liquidmetal_v1alpha1_search_agent_service.get_paginated_results(
                connect_protocol_version=1,
            )
        )
        assert_matches_type(
            LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsResponse,
            liquidmetal_v1alpha1_search_agent_service,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_paginated_results_with_all_params(self, client: Raindrop) -> None:
        liquidmetal_v1alpha1_search_agent_service = (
            client.liquidmetal_v1alpha1_search_agent_service.get_paginated_results(
                connect_protocol_version=1,
                organization_id="organization_id",
                page=0,
                page_size=0,
                request_id="request_id",
                user_id="user_id",
                connect_timeout_ms=0,
            )
        )
        assert_matches_type(
            LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsResponse,
            liquidmetal_v1alpha1_search_agent_service,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_paginated_results(self, client: Raindrop) -> None:
        response = client.liquidmetal_v1alpha1_search_agent_service.with_raw_response.get_paginated_results(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        liquidmetal_v1alpha1_search_agent_service = response.parse()
        assert_matches_type(
            LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsResponse,
            liquidmetal_v1alpha1_search_agent_service,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_paginated_results(self, client: Raindrop) -> None:
        with client.liquidmetal_v1alpha1_search_agent_service.with_streaming_response.get_paginated_results(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            liquidmetal_v1alpha1_search_agent_service = response.parse()
            assert_matches_type(
                LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsResponse,
                liquidmetal_v1alpha1_search_agent_service,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncLiquidmetalV1alpha1SearchAgentService:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_paginated_results(self, async_client: AsyncRaindrop) -> None:
        liquidmetal_v1alpha1_search_agent_service = (
            await async_client.liquidmetal_v1alpha1_search_agent_service.get_paginated_results(
                connect_protocol_version=1,
            )
        )
        assert_matches_type(
            LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsResponse,
            liquidmetal_v1alpha1_search_agent_service,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_paginated_results_with_all_params(self, async_client: AsyncRaindrop) -> None:
        liquidmetal_v1alpha1_search_agent_service = (
            await async_client.liquidmetal_v1alpha1_search_agent_service.get_paginated_results(
                connect_protocol_version=1,
                organization_id="organization_id",
                page=0,
                page_size=0,
                request_id="request_id",
                user_id="user_id",
                connect_timeout_ms=0,
            )
        )
        assert_matches_type(
            LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsResponse,
            liquidmetal_v1alpha1_search_agent_service,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_paginated_results(self, async_client: AsyncRaindrop) -> None:
        response = await async_client.liquidmetal_v1alpha1_search_agent_service.with_raw_response.get_paginated_results(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        liquidmetal_v1alpha1_search_agent_service = await response.parse()
        assert_matches_type(
            LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsResponse,
            liquidmetal_v1alpha1_search_agent_service,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_paginated_results(self, async_client: AsyncRaindrop) -> None:
        async with async_client.liquidmetal_v1alpha1_search_agent_service.with_streaming_response.get_paginated_results(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            liquidmetal_v1alpha1_search_agent_service = await response.parse()
            assert_matches_type(
                LiquidmetalV1alpha1SearchAgentServiceGetPaginatedResultsResponse,
                liquidmetal_v1alpha1_search_agent_service,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True
