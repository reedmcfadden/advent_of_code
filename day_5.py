#!/usr/bin/env python3

# returns the number of nice strings for part 1
def part_1(lines: str) -> int:
    # part 1 nice string requirements:
    # 1. at least 3 vowels
    # 2. at least 1 letter that appears twice in a row
    # 3. cannot contain the strings ab, cd, pq, or xy
    num_nice_strings = 0
    for line in lines:
        num_vowels = 0
        has_double_letter = False
        has_bad_string = False
        prev_char = None

        for c in line:
            if c in "aeiou":
                num_vowels += 1
            if c == prev_char:
                has_double_letter = True
            # if unallowed string found, break and stop processing this string
            if prev_char is not None and prev_char + c in ["ab", "cd", "pq", "xy"]:
                has_bad_string = True
                break

            # update prev char
            prev_char = c

        # determine if a good string was found
        if num_vowels >= 3 and has_double_letter and not has_bad_string:
            num_nice_strings += 1

    return num_nice_strings

def part_2(lines: str) -> int:
    # part 2 nice string requirements:
    # 1. at least 1 pair of any letters that appears twice in the string without overlapping
    # 2. at least 1 letter that appears with exactly one letter between them
    num_nice_strings = 0
    for line in lines:
        contains_non_overlapping_pair = False
        contains_sandwich_letter = False
        recent_duplicate_chars = 0
        pairs = dict()      # dict of pairs of chars and their counts

        # check each char, starting at the second char
        for i in range(1, len(line)):
            # if the new pair has non matching chars or there are no recent duplicate chars,
            # then add the pair to the dict and set duplicate chars if needed
            if line[i] != line[i-1] or recent_duplicate_chars <= 0:
                curr_pair = line[i-1:i+1]
                if (curr_pair[0] == curr_pair[1]):
                    recent_duplicate_chars = 2
                if curr_pair not in pairs:
                    pairs[curr_pair] = 1
                else:
                    pairs[curr_pair] += 1
                # if two of the same char pairs have been found, set the flag
                if pairs[curr_pair] >= 2:
                    contains_non_overlapping_pair = True

            # check every char for a sandwich letter
            if i >= 2 and line[i - 2] == line[i]:
                contains_sandwich_letter = True

            # decrement the recent duplicate chars each loop, as chars go out of range
            recent_duplicate_chars -= 1

        # if a nice string was found, increment the count
        if contains_non_overlapping_pair and contains_sandwich_letter:
            num_nice_strings += 1

    return num_nice_strings

def main():
    with open("./inputs/day_5.txt") as f:
        lines = f.readlines()

    # clean up the lines
    for line in lines:
        line.strip()

    part_1_num_nice_strings = part_1(lines)
    part_2_num_nice_strings = part_2(lines)

    print(f"Number of nice strings: {part_1_num_nice_strings}")
    print(f"Number of new nice strings: {part_2_num_nice_strings}")


if __name__ == "__main__":
    main()