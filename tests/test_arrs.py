from utils import arrs
import pytest

@pytest.mark.parametrize('some_list, index, expected', [
    ([1, 2, 3], 1, 2),
    ([1, 1, 2, 3], 0, 1),
    ([0, 1, 1, 2], -1, None)
])
def test_get(some_list, index, expected):
    assert arrs.get(some_list, index) == expected


def test_get_index_error():
    with pytest.raises(IndexError):
        arrs.get([], 0)

@pytest.mark.parametrize('cool, start, end, expect', [
    ([1, 2, 3, 4], 1, 3, [2, 3]),
    ([1, 2, 3], 1, 2, [2]),
    ([], 0, 1, []),
    ([0, 1, 2, 3, 4, 5], -4, -1, [2, 3, 4]),
    ([1, 2, 3], -5, None, [1, 2, 3])
])
def test_slice(cool, start, end, expect):
    assert arrs.my_slice(cool, start, end) == expect

