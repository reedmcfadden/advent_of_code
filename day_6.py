#!/usr/bin/env python3

# replace unnecessary instruction components, and split into tokens
# return command, start_coords, and end_coords
def get_command_and_coords_from_instruction(line:str):
    line = line.replace("turn ", "")
    line = line.replace("through ", "")
    line = line.replace(",", " ")
    tokens = line.split(" ")
    command = tokens.pop(0)
    start_coords = (tokens.pop(0), tokens.pop(0))
    end_coords = (tokens.pop(0), tokens.pop(0))
    return command, start_coords, end_coords

def part_one(lines: str) -> int:
    # create 1000x1000 array of bools (False = off, True = on)
    lights = [[False for x in range(1000)] for y in range(1000)]

    for line in lines:
        command, start_coords, end_coords = get_command_and_coords_from_instruction(line)

        for x in range(int(start_coords[0]), int(end_coords[0]) + 1):
            for y in range(int(start_coords[1]), int(end_coords[1]) + 1):
                if command == "on":
                    lights[x][y] = True
                elif command == "off":
                    lights[x][y] = False
                elif command == "toggle":
                    lights[x][y] = not lights[x][y]

    # count lights that are on
    on_lights = 0
    for x in range(1000):
        for y in range(1000):
            if lights[x][y]:
                on_lights += 1
            
    return on_lights;


def part_two(lines: str) -> int:
    # create 1000x1000 array of ints. 0 is the min brightness
    lights = [[0 for x in range(1000)] for y in range(1000)]

    for line in lines:
        command, start_coords, end_coords = get_command_and_coords_from_instruction(line)

        # execute the instructions
        for x in range(int(start_coords[0]), int(end_coords[0]) + 1):
            for y in range(int(start_coords[1]), int(end_coords[1]) + 1):
                if command == "on":
                    lights[x][y] += 1
                elif command == "off":
                    lights[x][y] = max(0, lights[x][y] - 1)
                elif command == "toggle":
                    lights[x][y] += 2

    # sum all the brightnesses
    total_brightness = 0
    for x in range(1000):
        for y in range(1000):
            total_brightness += lights[x][y]
            
    return total_brightness;


def main():
    lines = None
    with open("./inputs/day_6.txt", "r") as f:
        lines = f.readlines()

    on_lights = part_one(lines)
    total_brightness = part_two(lines)

    print(f"part one: there are {on_lights} lights on")
    print(f"part two: the total brightness is {total_brightness}")


if __name__ == "__main__":
    main()