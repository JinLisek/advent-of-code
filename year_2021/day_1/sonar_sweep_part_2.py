from typing import Sequence


def sonar_sweep_part_2(measurements: Sequence[int]) -> int:
    if len(measurements) < 4:
        return 0

    num_of_depth_window_increases = 0

    for i in range(len(measurements) - 3):
        current_sum = measurements[i] + measurements[i + 1] + measurements[i + 2]
        next_sum = measurements[i + 1] + measurements[i + 2] + measurements[i + 3]

        if next_sum > current_sum:
            num_of_depth_window_increases += 1

    return num_of_depth_window_increases


def main() -> None:
    with open(file="depth_measurements.txt", mode="r", encoding="utf-8") as f:
        measurements = list(map(int, f.read().split()))
    print(sonar_sweep_part_2(measurements=measurements))


if __name__ == "__main__":
    main()
