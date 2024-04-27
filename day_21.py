#!/usr/bin/env python3

# Notes
# - player and enemy (boss fight)
# - player always goes first
# - each attach reduces opponent's hp by 1
# - first character at or below 0 hp loses
# - damage dealt by an attacker each turn is equal
#   to the attackers dmg score - defender's armor score
# - attacker always deals at least 1 dmg
# - dmg and armor both start at 0
# - dmg and armor stats are the sum of all item stats
# - start with no items
# - player has 100 hp
# - have infinite gold
# - only one weapon, no dual-wielding
# - armor is optional, but can only use 1
# - can have 0-2 rings
# - any bought items MUST be used
# - shop only have one of each item

# Challenge
# - what is the least amount of gold you can spend and still win.
# - this is a knapsack problem, so probably need to use greedy

from math import ceil

SHOP_CONTENTS = '''
    Weapons:    Cost  Damage  Armor
    Dagger        8     4       0
    Shortsword   10     5       0
    Warhammer    25     6       0
    Longsword    40     7       0
    Greataxe     74     8       0

    Armor:      Cost  Damage  Armor
    Leather      13     0       1
    Chainmail    31     0       2
    Splintmail   53     0       3
    Bandedmail   75     0       4
    Platemail   102     0       5

    Rings:      Cost  Damage  Armor
    Damage +1    25     1       0
    Damage +2    50     2       0
    Damage +3   100     3       0
    Defense +1   20     0       1
    Defense +2   40     0       2
    Defense +3   80     0       3
'''

def main():
    lines = open('./inputs/day_21.txt', 'r').readlines()
    BASE_HP = 100
    # 1 weapon, 0-1 armor, 0-2 rings allowed
    # contains list of tuples of (hp, cost, dmg, armor)
    stat_combos = []

    # Get boss stats
    boss_stats = []
    for l in lines:
        l = l.strip()
        if not l: continue
        _, val = l.split(': ')
        boss_stats.append(int(val))
    lowest_gold_spent = 99999
    max_gold_spent = 0

    # Parse shop contents
    weapon_list = []
    armor_list = [('Nothing', 0, 0, 0)]
    ring_list = [('Nothing_1', 0, 0, 0), ('Nothing_2', 0, 0, 0)]
    curr_type = ""
    for l in SHOP_CONTENTS.split('\n'):
        l = l.strip()
        if not l: continue
        tokens = l.split()
        if ':' in tokens[0]:
            curr_type = tokens[0][0:-1]
            continue
        if curr_type == 'Weapons':
            weapon_list.append((tokens[0], int(tokens[1]), int(tokens[2]), int(tokens[3])))
        elif curr_type == 'Armor':
            armor_list.append((tokens[0], int(tokens[1]), int(tokens[2]), int(tokens[3])))
        else:
            ring_list.append((tokens[0] + tokens[1], int(tokens[2]), int(tokens[3]), int(tokens[4])))

    # Get all stat combos. Requirements: 1 weapon, 0-1 armor, 0-2 rings
    for w in weapon_list:
        for a in armor_list:
            for r1 in ring_list:
                for r2 in ring_list:
                    # If ring names are unique, add new combo. Weapon and armor will always be unique.
                    if r1[0] != r2[0]:
                        stat_combos.append(
                            (
                                BASE_HP,
                                w[1]+a[1]+r1[1]+r2[1],
                                w[2]+a[2]+r1[2]+r2[2],
                                w[3]+a[3]+r1[3]+r2[3],
                            )
                        )

    # Determine if each combo wins or loses. If winning combo has new lowest cost, save
    for sc in stat_combos:
        # dpt = damage per turn
        player_dpt = max(1, sc[2] - boss_stats[2])
        boss_dpt = max(1, boss_stats[1] - sc[3])
        player_turns_to_die = ceil(sc[0] / boss_dpt)
        boss_turns_to_die = ceil(boss_stats[0] / player_dpt)
        # Determines part 1 answer
        if boss_turns_to_die < player_turns_to_die:
            lowest_gold_spent = min(lowest_gold_spent, sc[1])
        # Determines part 2 answer
        if boss_turns_to_die > player_turns_to_die:
            max_gold_spent = max(max_gold_spent, sc[1])


    # TODO - finish up and print out answer
    print(f'Part 1 answer: {lowest_gold_spent}')
    print()
    print(f'Part 2 answer: {max_gold_spent}')

if __name__ == "__main__":
    main()