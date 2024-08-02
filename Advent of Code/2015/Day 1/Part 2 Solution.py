with open ('C:/Users/admin/Desktop/ADVENT OF CODE/2015/DAY 1/braces.txt', 'r') as braces:
    content = braces.read()

floor = 0
position  = 0

for i in content:
    if i == '(':
        floor += 1
        position += 1
    elif i == ')':
        floor -= 1
        position += 1
    if floor == -1:
        break

print(position)