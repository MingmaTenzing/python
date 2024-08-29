
# local scope
# if you define the variable inside a function you can use only within the function and innerfunction only. Not outside
def sum():
    x = 1+2
    def inner_Func():
        print(x)
    inner_Func()
    
sum()


# global scope 
#you need to define the variable in the python main body code.

x=400 

def myFunc():
    print(x)

myFunc()
print(x)

#if you want to create a global variable but it's inside the local scope then you can use the global keyword to make the variable global

def testing():
    global y
    y=300
testing()
print(y)

