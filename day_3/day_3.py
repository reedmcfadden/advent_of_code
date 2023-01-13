#!/usr/bin/env python3

def main():
    santa_curr_loc = (0,0)
    robot_curr_loc = (0,0)
    visited = set(santa_curr_loc)
    toggle = True

    # Read in all directions into 2d list
    with open("inputs/day_3.txt") as f:
        input = f.read()
        
    # Process each direction and add to set
    for direction in input:
        # Toggle between santa and robo santa
        mover_curr_loc = santa_curr_loc if toggle else robot_curr_loc

        if direction == '>':
            mover_curr_loc = (mover_curr_loc[0]+1, mover_curr_loc[1])
        elif direction == '<':
            mover_curr_loc = (mover_curr_loc[0]-1, mover_curr_loc[1])
        elif direction == '^':
            mover_curr_loc = (mover_curr_loc[0], mover_curr_loc[1]+1)
        elif direction == 'v':
            mover_curr_loc = (mover_curr_loc[0], mover_curr_loc[1]-1)
        else:
            print("Invalid direction")
            exit(1)

        # Update current location
        if toggle:
            santa_curr_loc = mover_curr_loc
        else:
            robot_curr_loc = mover_curr_loc

        visited.add(mover_curr_loc)
        toggle = not toggle

    print(f"Number of houses visited: {len(visited) - 1}")

if __name__ == "__main__":
    main()