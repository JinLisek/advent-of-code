import pytest
from year_2021.day_1.sonar_sweep_part_1 import sonar_sweep_part_1
from year_2021.day_1.sonar_sweep_part_2 import sonar_sweep_part_2


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
def test_given_measurements_sonar_sweep_part_1should_return_value(
    expected_value, measurements
):
    assert expected_value == sonar_sweep_part_1(measurements=measurements)


@pytest.mark.parametrize(
    "expected_value,measurements",
    [
        (0, []),
        (0, [1]),
        (0, [2, 1]),
        (0, [1, 2]),
        (0, [1, 2, 3]),
        (0, [1, 1, 1, 1]),
        (0, [2, 1, 1, 1]),
        (1, [1, 1, 1, 2]),
        (1, [1, 1, 1, 2, 1]),
        (1, [1, 1, 1, 1, 2]),
        (2, [1, 1, 1, 2, 2]),
        (2, [1, 1, 1, 2, 1, 2]),
        (3, [1, 1, 1, 2, 3, 4]),
    ],
)
def test_given_measurements_sonar_sweep_part_2_should_return_value(
    expected_value, measurements
):
    assert expected_value == sonar_sweep_part_2(measurements=measurements)
