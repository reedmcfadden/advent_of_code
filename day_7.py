#!/usr/bin/env python3

# Part 1
# 1. split instructions into source and destination
# 2. perform operations, if necessary
    # NOTE: FOR OPERATIONS TO BE PERFORMED, ALL OPERANDS MUST
    # HAVE A SIGNAL
# 3. store the value at the destination
# 4. remove instructions after they are performed
# 5. repeat until all instructions are performed

# Part 2
# Same as part 1, except that the signal provided to b is hardwired to the result of part 1 -- 46065
def main(part_2=False):
    lines = open("./inputs/day_7.txt").read().splitlines()

    instructions = [] # list of tuples ([tokens...], dest)
    inputs = {}

    # populate instructions and inputs
    for line in lines:
        source, dest = line.split(" -> ")
        source = source.split(" ")
        inputs[dest] = None
        # NOTE, for part 2
        if part_2 and dest == "b":
            inputs["b"] = 46065
            continue
        instructions.append((source, dest))

    while instructions:
        for instr in instructions:
            # check if all tokens in source have a signal before proceeding
            # else, skip to next instruction
            skip_this_instruction = False
            for tok in instr[0]:
                if tok in inputs and inputs[tok] is None:
                    skip_this_instruction = True
                    break
            if skip_this_instruction:
                continue

            if len(instr[0]) == 1:
                curr_op = instr[0][0]
                inputs[instr[1]] = int(curr_op) if curr_op not in inputs else inputs[curr_op]
                instructions.remove(instr)
            elif len(instr[0]) == 2:
                curr_op = instr[0][1]
                inputs[instr[1]] = ~int(curr_op) if curr_op not in inputs else ~inputs[curr_op]
                instructions.remove(instr)
            elif len(instr[0]) == 3:
                curr_op_1 = instr[0][0]
                curr_op_2 = instr[0][2]
                val1 = int(curr_op_1) if curr_op_1 not in inputs else inputs[curr_op_1]
                val2 = int(curr_op_2) if curr_op_2 not in inputs else inputs[curr_op_2]
                
                if instr[0][1] == "AND":
                    inputs[instr[1]] = val1 & val2
                elif instr[0][1] == "OR":
                    inputs[instr[1]] = val1 | val2
                elif instr[0][1] == "LSHIFT":
                    inputs[instr[1]] = val1 << val2
                elif instr[0][1] == "RSHIFT":
                    inputs[instr[1]] = val1 >> val2
                instructions.remove(instr)

    if not part_2:
        print(f"Part 1: signal provided to 'a' is -- {inputs['a']}")
    else:
        print(f"Part 2: signal provided to 'a' is -- {inputs['a']}")


if __name__ == "__main__":  
    main()
    main(True)