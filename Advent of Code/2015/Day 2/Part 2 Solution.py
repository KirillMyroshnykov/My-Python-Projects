def ribbon_dimension(l, w, h):
    return 2*l + 2*w + l*w*h


with open('C:/Users/admin/Desktop/ADVENT OF CODE/2015/DAY 2/dimensions.txt', 'r') as dimensions:
    dimensions = dimensions.read()

dimentional_list = dimensions.split('\n')

sizes = [sorted(list(map(int,i.split('x')))) for i in dimentional_list]

ribbon=0

for a,b,c in sizes:
    ribbon += ribbon_dimension(a, b, c)

print(ribbon)