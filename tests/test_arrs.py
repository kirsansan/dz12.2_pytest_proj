from utils import arrs


def test_get(get_data):
    assert arrs.get(get_data, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(get_data):
    assert arrs.my_slice(get_data, 1, 3) == [2, 3]
    assert arrs.my_slice(get_data, 1) == [2, 3, 4]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(get_data, -2, None) == [3, 4]
    assert arrs.my_slice(get_data, -6, None) == get_data