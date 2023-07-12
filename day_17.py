#!/bin/python

import itertools

def main():
    print("Day 17")

    lines = open("day_17.input", "r").readlines()
    containers = list()
    num_combinations = 0
    num_combinations_2 = 0
    num_combinations_2_len = 0

    for line in lines:
        containers.append(int(line.strip()))

    # Get all combinations
    for i in range(1, len(containers)):
        curr_combs = list(itertools.combinations(containers, i))
        for c in curr_combs:
            # Part 1
            if sum(c) == 150:
                num_combinations += 1
            # Part 2
            if sum(c) == 150 and (num_combinations_2_len == 0 or num_combinations_2_len == len(c)):
                num_combinations_2_len = len(c)
                num_combinations_2 += 1

    print(num_combinations)
    print(num_combinations_2)

if __name__ == "__main__":
    main()
