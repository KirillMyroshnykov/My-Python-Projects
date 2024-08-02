import numpy

with open('C:/Users/admin/Desktop/ADVENT OF CODE/2015/DAY 6/puzzle_input.txt') as f:
    strings = f.read()

strings_list = strings.split('\n')
instructions = [string.split() for string in strings_list]

for lst in instructions:
    for element in lst:
        if element == 'turn':
            lst.remove(element)
        if element == 'through':
            lst.remove(element)

array = numpy.zeros((1000,1000))


for i in instructions:
    x1, y1 = [int(x) for x in i[1].split(',')]
    x2, y2 = [int(x) for x in i[2].split(',')]
    command = i[0]
    if command=='on':
        for x in range(x1,x2+1):
            for y in range(y1, y2+1):
                array[x][y]+=1
    elif command=='off':
        for x in range(x1,x2+1):
            for y in range(y1, y2+1):
                if array[x][y] > 0:
                    array[x][y] -= 1
    else:
        for x in range(x1,x2+1):
            for y in range(y1, y2+1):
                array[x][y] += 2

count = 0
for x in array:
    count += sum(x)

print(int(count))