with open('C:/Users/admin/Desktop/ADVENT OF CODE/2015/DAY 3/directions.txt', 'r') as directions:
    directions = directions.read()

x = 0
y = 0

santa_trip = {(x, y): 1}

for i in directions:
    if i == '^':
        y += 1
    elif i == 'v':
        y -= 1
    elif i == '>':
        x += 1
    else:
        x -= 1
    santa_trip[(x,y)] = santa_trip.get((x,y), 0) + 1

print(len(santa_trip))
