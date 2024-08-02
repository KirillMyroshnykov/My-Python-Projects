with open ('C:/Users/admin/Desktop/ADVENT OF CODE/2015/DAY 1/braces.txt', 'r') as braces:
    content = braces.read()

left_braces = [i for i in content if i == '(']
right_braces = [i for i in content if i == ')']

#print(len(left_braces))
#print(len(right_braces))

print(len(left_braces) - len(right_braces))