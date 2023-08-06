from utils import arrs
import pytest

def test_get():
    assert arrs.get([1, 2, 3], 1, 2) == 2


def test_get_index_error():
    with pytest.raises(IndexError):
        arrs.get([], 0)

def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
