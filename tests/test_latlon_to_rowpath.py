import pytest
from src.latlon_to_rowpath import _validate_input, latlon_to_rowpath


# tests for _validate_input (invalid input)
@pytest.mark.parametrize(
    "test_input",
    [
        # case 1
        {"lat": 300.0, "lon": 600.0, "mode": "X"},
        # case 2
        {"lat": 75.0, "lon": 600.0, "mode": "D"},
        # case 3
        {"lat": 75.0, "lon": -400.0, "mode": "A"},
        # case 4
        {"lat": "hi", "lon": 600.0, "mode": "Z"},
        # case 5
        {"lat": 300.0, "lon": "abc", "mode": "a"},
    ],
)
def test_validate_input_by_invalid_input(test_input):
    with pytest.raises(ValueError):
        _validate_input(**test_input)

# tests for _validate_input (valid input)
@pytest.mark.parametrize(
    "test_input",
    [
        # case 1
        {"lat": 75.0, "lon": 20.0, "mode": "D"},
        # case 2
        {"lat": 20.0, "lon": -180.0, "mode": "A"},
    ],
)
def test_validate_input_by_valid_input(test_input):
    assert _validate_input(**test_input)

# tests for latlon_to_rowpath
# TBD
