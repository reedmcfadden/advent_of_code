#!/bin/python

import re

def valid_password(curr):
    # 1. Check for disallowed chars
    disallowed = ['i', 'o', 'l']
    for c in disallowed:
        if c in curr:
            return False

    # 2. Check that there are two pairs of the same char. ex: aabb, oonnhena
    doubles = re.findall(r"((\w)\2)", curr)
    if len(doubles) < 2:
        return False

    # 3. Check for at least one straight of at least 3 chars. ex: abc, cdefxx
    for i in range(len(curr) - 3):
        first = curr[i]
        second = chr(ord(first) + 1)
        third = chr(ord(second) + 1)

        if curr[i + 1] == second and curr[i + 2] == third:
            return True

    return False

def next_password(curr):
    pwd_list = list(curr)
    done = False
    curr = len(pwd_list) - 1
    while not done:
        if pwd_list[curr] == 'z':
            pwd_list[curr] = 'a'
            curr = curr - 1
        else:
            pwd_list[curr] = chr(ord(pwd_list[curr]) + 1)
            done = True
        if curr < 0:
            print("CRITICAL ERROR: Curr is somehow below 0")
            exit

    return ''.join(pwd_list)

def main():
    curr = "cqjxjnds"
    while not valid_password(curr):
        curr = next_password(curr)
    print(f"1. Valid password is {curr}")

    curr = next_password(curr)
    while not valid_password(curr):
        curr = next_password(curr)
    print(f"2. Valid password is {curr}")

if __name__ == "__main__":
    main()
