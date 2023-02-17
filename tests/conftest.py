""" Pytest configuration tests fixtures and other helper methods """

import pytest

from example.web import Web


@pytest.fixture()
def client():
    """Get a web client"""
    yield Web()
