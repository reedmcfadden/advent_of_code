#!/usr/bin/env python3

import itertools

def main():
    people = set()
    rel_map = {}
    max_happiness = -9999999

    # parse. populate people set and rel_map
    f = open("./inputs/day_13.txt", 'r')
    for line in f.readlines():
        line = line.strip()[0:-1]   # strip whitespace and trim trailing period
        if not line:
            continue
        tokens = line.split()
        person = tokens[0]
        rel_person = tokens[-1]
        value = int(tokens[3])
        modifier = tokens[2]
        happiness = value if modifier != "lose" else value * -1

        # add both people to the set
        people.add(person)
        people.add(rel_person)

        # add new relationship to the map
        # if this is a newly encountered person, initialize their map
        if person not in rel_map.keys():
            rel_map[person] = {"me": 0}     # add me for part 2. will not affect part 1
        rel_map[person][rel_person] = happiness

#        print(f"extracted... person: {person} | rel_person: {rel_person} | happiness: {happiness}")
#        print(f"relationship map is: {rel_map}")
#    print(f"person set is: {people}")

    # add a relationship map for "me" for part 2. comment out for part 1 result
    rel_map["me"] = {}
    for p in people:
        rel_map["me"][p] = 0
    people.add("me")

    # generate all permutations of seating arrangements in list form
    perms = itertools.permutations(people)
    
    # iterate over each list permutation and calculate the total happiness
    # if it is a new max, save it off
    perms_list = list(perms)
    list_len = len(perms_list[0])
    for curr in perms_list:
        curr_happiness = 0
        for i in range(list_len):
            left = i - 1 if i - 1 >= 0 else list_len - 1
            right = (i + 1) % list_len
#            print(f"left: {left} | curr: {i} | right: {right}")
            curr_happiness = curr_happiness + rel_map[curr[i]][curr[left]]
            curr_happiness = curr_happiness + rel_map[curr[i]][curr[right]]
        max_happiness = max(curr_happiness, max_happiness)
    
    print(f"max happiness: {max_happiness}")

if __name__ == "__main__":
    main()
