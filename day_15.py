#!/bin/python

# Notes:
# must find right balance of ingredients
# must balance ingredients between exactly 100 teaspoons
# input will consist of remaining ingredients and their properties

# the properties are:
# - capacity (milk absorption)
# - durability (how well the cookie stays together when full of milk)
# - flavor (how tasty)
# - texture (how it improves the cookie's feel)
# - calories (how many calories it adds to the cookie)
# 
# ingredients can only be used in whole-teaspoon amounts -- no fractions
# 
# the score of each property can be calculated by multiplying the property value of
# each ingredient by the amount used, then summing those together
#
# the total score is equal to the multiplication of all the  overall property
# scores, except calories 
# 

def main():
    print("Day 15: Science for Hungry People")
    inLines = open("day_15.input", "r").readlines()
    tokens = list()
    part_1_best_score = 0
    part_2_best_score = 0


    # tokenize each line and delete empty list at end
    for line in inLines:
        tokens.append(line.split())
    del tokens[-1]

    # trim off colons and commas
    for ingredient in tokens:
        ingredient[0] = ingredient[0][:-1]
        ingredient[2] = int(ingredient[2][:-1])
        ingredient[4] = int(ingredient[4][:-1])
        ingredient[6] = int(ingredient[6][:-1])
        ingredient[8] = int(ingredient[8][:-1])
        ingredient[10] = int(ingredient[10])

#    print(tokens)
#    input()

    for sprinkles in range(100):
        for peanut_butter in range(100 - sprinkles):
            for frosting in range(100 - sprinkles - peanut_butter):
                    # set sugar to remaining amount
                    sugar = 100 - sprinkles - peanut_butter - frosting

                    # calculate total attribute scores
                    curr_capacity = (tokens[0][2] * sprinkles) + (tokens[1][2] * peanut_butter) + (tokens[2][2] * frosting) + (tokens[3][2] * sugar)
                    curr_durability = (tokens[0][4] * sprinkles) + (tokens[1][4] * peanut_butter) + (tokens[2][4] * frosting) + (tokens[3][4] * sugar)
                    curr_flavor = (tokens[0][6] * sprinkles) + (tokens[1][6] * peanut_butter) + (tokens[2][6] * frosting) + (tokens[3][6] * sugar)
                    curr_texture = (tokens[0][8] * sprinkles) + (tokens[1][8] * peanut_butter) + (tokens[2][8] * frosting) + (tokens[3][8] * sugar)
                    curr_calories = (tokens[0][10] * sprinkles) + (tokens[1][10] * peanut_butter) + (tokens[2][10] * frosting) + (tokens[3][10] * sugar)

                    # set negatives to 0
                    curr_capacity = max(0, curr_capacity)
                    curr_durability = max(0, curr_durability)
                    curr_flavor = max(0, curr_flavor)
                    curr_texture = max(0, curr_texture)

                    # calculate total score
                    curr_total_score = curr_capacity * curr_durability * curr_flavor * curr_texture

                    # if new total score is better, set it as best score
                    if curr_total_score > part_1_best_score:
                        part_1_best_score = curr_total_score
                    if curr_total_score > part_2_best_score and curr_calories == 500:
                        part_2_best_score = curr_total_score

    print("Part 1 best score: ", part_1_best_score)
    print("Part 2 best score: ", part_2_best_score)

if __name__ == '__main__':
    main()
