import pytest

DATA = [1, 2, 3, 4]
@pytest.fixture
def get_data():
        return DATA