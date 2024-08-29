class Person:
    def __init__(person, first_name, last_name):
        person.first_name = first_name
        person.last_name = last_name
        
    def printName(person):
        print(person.first_name, person.last_name)

class Student(Person):
    pass


student1 = Student("toyota", "Aurion")

student1.printName()

