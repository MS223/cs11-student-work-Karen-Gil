def max_value(integer):
    print range(1,integer +1)
max_value(10)

list1 = [4,5,15,11,23,42]
list2 = [1,8,7,16,7,35]
print
def compare_lists():
    for x in list1:
     if x > list2[list1.index(x)]:
        print x
     else:
        print list2[list1.index(x)]
compare_lists()

def swapping_star():
    width= input("How wide")
    height= input("How tall")
    for x in range(0,height):
        if x % 2 == 1:
            print (width/2)* '*-'
        else:
            print(width/2)* "-*"
swapping_star()
