import pytest

from src.models.extreme_point import ExtremePoint


def test_extreme_point_valid():
    point = ExtremePoint(1, 2, 3)

    assert point.x == 1
    assert point.y == 2
    assert point.z == 3


def test_extreme_point_negative_coordinates():
    with pytest.raises(ValueError):
        ExtremePoint(-1, 2, 3)
