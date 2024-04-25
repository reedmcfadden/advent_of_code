#!/usr/bin/env python3

def main():
    time_limit = 2503
    greatest_distance = 0
    greatest_points = 0

    # info order: 0. name, 1. speed, 2. speed_duration, 3. rest_duration, 4.
    # cycle_duration, 5. curr_distance, 6. points
    reindeer_info = []

    f = open('./inputs/day_14.txt', 'r')
    for line in f.readlines():
        line = line.strip()
        tokens = line.split()
        name = tokens[0]
        speed = int(tokens[3])
        speed_duration = int(tokens[6])
        rest_duration = int(tokens[-2])
        print(f'extracted: {name}, {speed}, {speed_duration}, {rest_duration}')
        reindeer_info.append([name, speed, speed_duration, rest_duration, speed_duration + rest_duration, 0, 0])

    # Part 1
    for r in reindeer_info:
        fly_rest_cycle_duration = r[2] + r[3]
        fly_rest_cycle_distance = r[1] * r[2]
        num_cycles = time_limit // fly_rest_cycle_duration
        remainder_duration = time_limit % fly_rest_cycle_duration
        remainder_distance = min(fly_rest_cycle_distance, remainder_duration * r[1])
        curr_distance = num_cycles * fly_rest_cycle_distance + remainder_distance
        greatest_distance = max(curr_distance, greatest_distance)
    print(f'Part 1: greatest distance is {greatest_distance}')

    # Part 2
    for i in range(time_limit):
        lead_distance = 0
        for r in reindeer_info:
            if (i % r[4]) < r[2]:
                r[5] = r[5] + r[1]
            lead_distance = max(lead_distance, r[5])
        for r in reindeer_info:
            if r[5] == lead_distance:
                r[6] = r[6] + 1

    for r in reindeer_info:
        greatest_points = max(greatest_points, r[6])
    print(f'Part 2: greatest points is {greatest_points}')

    return

if __name__ == "__main__":
    main()
