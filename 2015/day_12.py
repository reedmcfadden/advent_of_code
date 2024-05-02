#!/usr/bin/env python3

import json

count = 0

def loop_list(curr):
    global count
    for item in curr:
        if item.__class__ == int:
            print(f'found int: {item}')
            count = count + item
        elif item.__class__ == list:
            print(f'found list: {item}')
            loop_list(item)
        elif item.__class__ == dict:
            print(f'found dict: {item}')
            loop_dict(item)

def loop_dict(curr):
    global count
    print("INSIDE DICTIONARY FUNCTION")

    # For part 2: if dict contains a value "red" anywhere, skip it entirely
    # Comment out if part 1 answer is required
    for key, value in curr.items():
        if value == "red":
            return
            
    for key, value in curr.items():
        if key.__class__ == int:
            print(f'found int: {key}')
            count = count + key
        if value.__class__ == int:
            print(f'found int: {value}')
            count = count + value
        elif value.__class__ == list:
            print(f'FOUND list: {value}')
            loop_list(value)
        elif value.__class__ == dict:
            print(f'found dict: {value}')
            loop_dict(value)

def main():
    f = open("./inputs/day_12.txt")

    json_data = json.load(f)
    for i in json_data:
        i_type = type(i)
        print(f'{i_type}')
        if i_type is list:
            loop_list(i)
        elif i_type is dict:
            loop_dict(i)
        else:
            print('Error: found other')

    print(f'count is: {count}')

if __name__ == "__main__":
    main()
