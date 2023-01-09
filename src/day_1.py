def main():

    with open("inputs/day_1_input.txt") as f:
        input = f.read()

    up = 0
    down = 0
    pos = 0
    enter_basement_pos = None

    for i in input:
        pos += 1

        if i == '(':
            up += 1
        elif i == ')':
            down += 1
        else:
            print("Invalid character")
            exit(1)

        if up - down == -1 and enter_basement_pos is None:
            enter_basement_pos = pos
            

    print(f"Up: {up}")
    print(f"Down: {down}")
    print(f"Final Floor: {up - down}")
    print(f"Basement entered at pos: {enter_basement_pos}")


if __name__ == main():
    main()