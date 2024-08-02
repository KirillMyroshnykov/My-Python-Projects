def bread(func):
    def wrapper():
        print ("</''''''\>") #before func call
        func()
        print ("<\______/>") #after func call
    return wrapper

def vegetables(func):
    def wrapper():
        print ("#помидорка#")
        func()
        print ("~лист салата~")
    return wrapper

@bread
@vegetables
def sandwich(food="--ветчина--"):
    print (food)
# Фактически код код выше означает следующее:
# sandwich = bread(vegetables(sandwich))

sandwich()