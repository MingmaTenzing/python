import json

class Person: 
    def __init__(myObject, name, age, email) :
        myObject.name = name
        myObject.age = age
        myObject.email = email
        
    def __str__(myObject):
        return f"{myObject.name}  ....{myObject.age}"

p1 = Person("Mingma",23, "mingmatenzing@gmail.com")
p2 = Person("Tenzing",20,"tenz@gmail.com")


y = json.dumps(p1)
print(y)