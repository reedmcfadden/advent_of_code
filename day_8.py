#!/usr/bin/env python3

def main():
    lines = open("./inputs/day_8.txt").read().splitlines()
    num_code_chars = 0
    num_mem_chars = 0

    # Part 1
    for line in lines:
        num_code_chars += len(line)

        # chars in memory counting:
        # 1. don't count the enclosing quotes
        # 2. count only one char for escaped char sequences
        # 3. count only one char for hex char sequences
        num_mem_chars += len(line) - 2

        i = 0
        while i < len(line) - 2:
            if line[i] == "\\" and (line[i+1] == "\\" or line[i+1] == "\""):
                num_mem_chars -= 1
                i += 2
            elif line[i] == "\\" and line[i+1] == "x":
                num_mem_chars -= 3
                i += 4
            else:
                i += 1

    # Part 2
    # start num encoded chars at num_code_chars
    num_encoded_chars = num_code_chars
    for line in lines:
        # add 2 for enclosing quotes for each line
        num_encoded_chars += 2
        i = 0
        while i < len(line):
            if line[i] == "\\" or line[i] == "\"":
                num_encoded_chars += 1
            i += 1

    print(f"Part 1:")
    print(f"num_code_chars: {num_code_chars}")
    print(f"num_mem_chars: {num_mem_chars}")
    print(f"num_code_chars - num_mem_chars: {num_code_chars - num_mem_chars}")
    print()
    print(f"Part 2:")
    print(f"num_encoded_chars: {num_encoded_chars}")
    print(f"num_encoded_chars - num_code_chars: {num_encoded_chars - num_code_chars}")
            

if __name__ == "__main__":
    main()