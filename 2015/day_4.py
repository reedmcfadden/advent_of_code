#!/usr/bin/env python3

import hashlib

def main():
    secret_key = None
    required_prefix = "000000"
    search_range = 100000000

    # Retrieve the secret key
    with open("./inputs/day_4.txt") as f:
        secret_key = f.read().strip()

    # Brute force loop until the hash that starts with the required prefix is found
    for i in range(search_range):
        curr_key = secret_key + str(i)
        md5_hash = hashlib.md5(curr_key.encode("utf-8")).hexdigest()

        # Key found, print the results
        if md5_hash.startswith(required_prefix):
            print(f"Found the key number: {i}")
            print(f"Found the total key: {curr_key}")
            print(f"Hash: {md5_hash}")
            break


if __name__ == "__main__":
    main()