list1 =[1,2,3,4]
list2=[3,4,5,6]
this_set =set()

for x in list1 + list2:
    square = x*x
    this_set.add(square)



print(this_set)