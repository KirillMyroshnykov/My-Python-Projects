with open('C:\\Users\\admin\\Desktop\\ADVENT OF CODE\\2015\\DAY 3\\directions.txt', 'r') as directions:
    directions = directions.read()

santa_moves = []
robot_moves = []

santa_moves.append(directions[::2])
robot_moves.append(directions[1::2])

santa_moves = ''.join(santa_moves)
robot_moves =''.join(robot_moves)

x1 = 0
y1 = 0

x2 = 0
y2 = 0

santa_trip = {(x1, y1): 1}
robot_trip = {(x2, y2): 1}

for i in santa_moves:
    if i == '^':
        y1 += 1
    elif i == 'v':
        y1 -= 1
    elif i == '>':
        x1 += 1
    else:
        x1 -= 1
    santa_trip[(x1,y1)] = santa_trip.get((x1,y1), 0) + 1

for i in robot_moves:
    if i == '^':
        y2 += 1
    elif i == 'v':
        y2 -= 1
    elif i == '>':
        x2 += 1
    else:
        x2 -= 1
    robot_trip[(x2,y2)] = robot_trip.get((x2,y2), 0) + 1

house_count = len(santa_trip)

for key in robot_trip.keys():
    if key not in santa_trip.keys():
        house_count += 1

print(house_count)