with open('C:\\Users\\admin\\Desktop\\ADVENT OF CODE\\2015\\DAY 5\\puzzle_input.txt', 'r') as f:
    strings = f.read()

strings_list = strings.split('\n')

vowels = 'aeiou'

vowels_counter, double_letter_counter, forbidden_symbols_counter, nice_strings, naughty_strings = 0, 0, 0, 0, 0

forbidden_symbols = ['ab', 'cd', 'pq', 'xy']

for string in strings_list:
    for char in string:
        if char in vowels:
            vowels_counter += 1
        if char * 2 in string:
            double_letter_counter += 1

    for symbol in forbidden_symbols:
        if symbol in string:
            forbidden_symbols_counter += 1

    if vowels_counter >= 3 and double_letter_counter >= 1 and forbidden_symbols_counter == 0:
        nice_strings += 1
    else:
        naughty_strings += 1

    vowels_counter, double_letter_counter, forbidden_symbols_counter = 0, 0, 0

print(f'The number of nice strings: {nice_strings}')
print(f'The number of naughty strings: {naughty_strings}')