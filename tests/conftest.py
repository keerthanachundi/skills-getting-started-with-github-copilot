import copy
import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


ORIGINAL_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture
def client():
    """Provide a TestClient for the FastAPI app."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory activities before each test for isolation."""
    activities.clear()
    activities.update(copy.deepcopy(ORIGINAL_ACTIVITIES))
    yield
    activities.clear()
    activities.update(copy.deepcopy(ORIGINAL_ACTIVITIES))
