import pytest

from garden_todo_backend.core.garden_time import GardenTime

def test_create_garden_time_from_start_and_end():
    valid_month = GardenTime(5, 6)
    assert valid_month.start_month == 5
    assert valid_month.end_month == 6

def test_create_garden_time_from_boundary_values():
    valid_month = GardenTime(1, 12)
    assert valid_month.start_month == 1
    assert valid_month.end_month == 12

def test_create_garden_time_from_end_before_start():
    backwards_month = GardenTime(6, 5)
    assert backwards_month.start_month == 6
    assert backwards_month.end_month == 5

def test_create_garden_time_from_invalid_start():
    with pytest.raises(ValueError):
        GardenTime(0, 5)
    with pytest.raises(ValueError):
        GardenTime(-1, 5)
    with pytest.raises(ValueError):
        GardenTime(13, 5)

def test_create_garden_time_from_invalid_end():
    with pytest.raises(ValueError):
        GardenTime(1, -1)
    with pytest.raises(ValueError):
        GardenTime(1, 0)
    with pytest.raises(ValueError):
        GardenTime(1, 13)