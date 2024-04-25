#!/usr/bin/env python3

import time


def look_say_encode(seq : list) -> list:
    prev_char = seq[0]
    result = []
    count = 1
    for i in range(1, len(seq)):
        if seq[i] == prev_char:
            count += 1
        else:
            result.append(str(count))
            result.append(prev_char)
            count = 1
            prev_char = seq[i]
    result.append(str(count))
    result.append(prev_char)
    return result


# TODO implement w/ regex
def look_say_regex_encode(seq : str) -> str:
    print("TODO")


def main():
    seq = open("./inputs/day_10.txt").read().strip()
    lseq = list(seq)
    part_1_num_loops = 40
    part_2_num_loops = 50

    # Part 1
    start = time.time()
    for i in range(part_1_num_loops):
        lseq = look_say_encode(lseq)
    print(f"Part 1 answer is: {len(lseq)}")
    print(f"run time: {time.time() - start}")

    # Part 2
    lseq = list(seq)
    start = time.time()
    for i in range(part_2_num_loops):
        lseq = look_say_encode(lseq)
    print(f"Part 2 answer is: {len(lseq)}")
    print(f"run time: {time.time() - start}")

    
if __name__ == "__main__":
    main()