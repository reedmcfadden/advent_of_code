#!/bin/python

def main():
    print("Day 16!")

    # Things detected by MFCSAM
    things_detected = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    lines = open("day_16.input", "r").readlines()

    # for part 1
    sue_list = list()
    # for part 2 
    sue_list_2 = list()

    print(things_detected)
    print(things_detected["cats"])

    for line in lines:
        line = line.strip()
        tokens = line.split()
        
        sue_no = tokens[1][:-1]

        thing_1_name = tokens[2][:-1]
        thing_1_val = int(tokens[3][:-1])

        thing_2_name = tokens[4][:-1]
        thing_2_val = int(tokens[5][:-1])

        thing_3_name = tokens[6][:-1]
        thing_3_val = int(tokens[7])

        print(things_detected[thing_1_name], things_detected[thing_2_name], things_detected[thing_3_name])

#        # part 1
#        if thing_1_val != things_detected[thing_1_name]:
#            continue
#        if thing_2_val != things_detected[thing_2_name]:
#            continue
#        if thing_3_val != things_detected[thing_3_name]:
#            continue
#        sue_list.append(sue_no)

        # part 2
        if thing_1_name == "cats" or thing_1_name == "trees": 
            if thing_1_val < things_detected[thing_1_name]:
                continue
        elif thing_1_name == "pomeranians" or thing_1_name == "goldfish": 
            if thing_1_val > things_detected[thing_1_name]:
                continue
        elif thing_1_val != things_detected[thing_1_name]:
            continue

        if thing_2_name == "cats" or thing_2_name == "trees": 
            if thing_2_val < things_detected[thing_2_name]:
                continue
        elif thing_2_name == "pomeranians" or thing_2_name == "goldfish": 
            if thing_2_val > things_detected[thing_2_name]:
                continue
        elif thing_2_val != things_detected[thing_2_name]:
            continue

        if thing_3_name == "cats" or thing_3_name == "trees": 
            if thing_3_val < things_detected[thing_3_name]:
                continue
        elif thing_3_name == "pomeranians" or thing_3_name == "goldfish": 
            if thing_3_val > things_detected[thing_3_name]:
                continue
        elif thing_3_val != things_detected[thing_3_name]:
            continue
        sue_list_2.append(sue_no)

    print(sue_list)
    print(sue_list_2)

if __name__ == "__main__":
    main()
