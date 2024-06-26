# This file was auto-generated by Fern from our API Definition.

import os

import pytest
from seed.client import AsyncSeedEnum, SeedEnum


@pytest.fixture
def client() -> SeedEnum:
    return SeedEnum(base_url=os.getenv("TESTS_BASE_URL"))


@pytest.fixture
def async_client() -> AsyncSeedEnum:
    return AsyncSeedEnum(base_url=os.getenv("TESTS_BASE_URL"))
