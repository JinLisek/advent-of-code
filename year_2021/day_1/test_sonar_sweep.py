import pytest
from year_2021.day_1.sonar_sweep import sonar_sweep


@pytest.mark.parametrize(
    "expected_value,measurements",
    [
        (0, []),
        (0, [1]),
        (0, [5, 4, 3]),
        (1, [1, 2]),
        (1, [2, 1, 3]),
        (1, [1, 2, 1]),
        (2, [3, 4, 5]),
        (2, [3, 4, 3, 5]),
    ],
)
def test_given_measurements_should_return_value(expected_value, measurements):
    assert expected_value == sonar_sweep(measurements=measurements)
