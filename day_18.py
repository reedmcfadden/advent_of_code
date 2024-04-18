# 100 x 100 grid
# animated

# each light's state is determined by curron state plus num neighbors that are ON
    # an on light stays on when 2 or 3 neighors are on, and turns off otherwise
    # an off light turns on if exactly 3 neights are on, otherwise it stays off

# all lights update based on the CURRENT state. then they all update to the NEXT state.
# this means that a current and next 2x2 array needs to be maintained, so that 
# states are not changed before all next states are determined.

import copy

def main():
    # Read in input
    lines = open('day_18.input', 'r').readlines()

    # Create necessary lists
    curr_state_list = []
    next_state_list = []
    neighbor_move_list = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]
    ]

    # Populate curr_state_list and next_state_list with input of the initial state
    for x, l in enumerate(lines):
        l = l.strip()
        curr_state_list.append(list(l))
        next_state_list.append(list(l))

    # Deterine the grid state after 100 (n) aplications of the stated rules.
    for _ in range(100):
        for x in range(100):
            for y in range(100):
                num_on = 0

                for x_mod, y_mod in neighbor_move_list:
                    curr_x = x+x_mod
                    curr_y = y+y_mod
                    if curr_x < 0 or curr_x > 99 or curr_y < 0 or curr_y > 99:
                        continue
                    if curr_state_list[curr_x][curr_y] == '#':
                        num_on += 1
                
                if curr_state_list[x][y] == '#' and num_on == 2 or num_on == 3:
                    next_state_list[x][y] = '#'
                elif curr_state_list[x][y] == '.' and num_on == 3:
                    next_state_list[x][y] = '#'
                else:
                    next_state_list[x][y] = '.'
        curr_state_list = copy.deepcopy(next_state_list)

    total_on = 0
    for r in curr_state_list:
        for c in r:
            if c == '#':
                total_on += 1

    print(f'The total number of lights on after 100 steps: {total_on}')

if __name__ == '__main__':
    main()