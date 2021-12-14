from typing import Sequence


def sonar_sweep_part_1(measurements: Sequence[int]) -> int:
    previous_meas = None
    num_of_depth_increases = 0

    for meas in measurements:
        if previous_meas is not None and previous_meas < meas:
            num_of_depth_increases += 1
        previous_meas = meas
    return num_of_depth_increases


def main() -> None:
    with open(file="depth_measurements.txt", mode="r", encoding="utf-8") as f:
        measurements = list(map(int, f.read().split()))
    print(sonar_sweep_part_1(measurements=measurements))


if __name__ == "__main__":
    main()
