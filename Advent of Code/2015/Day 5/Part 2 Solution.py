with open('C:/Users/admin/Desktop/ADVENT OF CODE/2015/DAY 5/puzzle_input.txt') as f:
    puzzle_input = f.read()

strings_list = puzzle_input.split('\n')

def is_pair(string):
    for i in range(len(string)-3):
        if string[i:i+2] in string[i+2:]:
            return True
    return False

def in_between(string):
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False

nice_counter, naughty_counter = 0, 0

for string in strings_list:
    if is_pair(string) and in_between(string):
        nice_counter += 1
    else:
        naughty_counter += 1

print(f'Nice strings: {nice_counter} \nNaughty strings: {naughty_counter}')