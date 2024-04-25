#!/usr/bin/env python3

def part_1():
    lines = open('./inputs/day_19.txt', 'r').readlines()
    medicine_molecule = lines.pop()
    replacements_list = []
    distinct_molecules = set()

    for l in lines:
        l = l.strip()
        if not l:
            continue
        tokens = l.split(' ')
        replacements_list.append((tokens[0], tokens[-1]))

    for i in range(len(medicine_molecule)):
        for _from, _to in replacements_list:
            molecule_len = len(_from)
            if _from == medicine_molecule[i:i+molecule_len]:
                distinct_molecules.add(
                    medicine_molecule[0:i]
                    + _to
                    + medicine_molecule[i+molecule_len:]
                )

    print(f'Part 1 answer: {len(distinct_molecules)}')

def main():
    part_1()

if __name__ == "__main__":
    main()