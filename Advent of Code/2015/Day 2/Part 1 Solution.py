def surface_area(l, w, h):
    return 3*l*w + 2*w*h + 2*h*l


with open('C:/Users/admin/Desktop/ADVENT OF CODE/2015/DAY 2/dimensions.txt', 'r') as dimensions:
    dimensions = dimensions.read()

dimentional_list = dimensions.split('\n')

sizes = [sorted(list(map(int,i.split('x')))) for i in dimentional_list]

square=0

for a,b,c in sizes:
    square += surface_area(a, b, c)

print(square)