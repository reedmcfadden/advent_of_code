#!/usr/bin/env python3

def part_1():
    target_num_presents = int(open('./inputs/day_20.txt', 'r').readline().strip())
    # Set num_houses to target number of presents / 10 b/c every house will have
    # house number * 10 presents delivered.
    num_houses = target_num_presents // 10
    house_presents = [0] * num_houses
    lowest_qualifying_house = target_num_presents
    # Loop through each elf, adding their presents to each house sequentially
    # If a better lowest qualifying house is found, update
    for i in range(1, num_houses):
        for j in range(i, num_houses, i):
            house_presents[j] += i*10
            if house_presents[j] >= target_num_presents and j < lowest_qualifying_house:
                lowest_qualifying_house = j
    print(f'Part 1 answer is: {lowest_qualifying_house}')

# Same as part one, except elf number * 11 presents are delivered at each respective house
# and each elf only delivers presents to 50 houses
def part_2():
    target_num_presents = int(open('./inputs/day_20.txt', 'r').readline().strip())
    num_houses = target_num_presents // 10
    house_presents = [0] * num_houses
    lowest_qualifying_house = target_num_presents
    for i in range(1, num_houses):
        deliveries = 0
        for j in range(i, num_houses, i):
            deliveries += 1
            house_presents[j] += i*11
            if house_presents[j] >= target_num_presents and j < lowest_qualifying_house:
                lowest_qualifying_house = j
            if deliveries >= 50:
                break
    print(f'Part 2 answer is: {lowest_qualifying_house}')

def main():
    part_1()
    print()
    part_2()

if __name__ == "__main__":
    main()