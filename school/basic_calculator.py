

def main():
    arithmetic_operation = str(input("What you wnat to do, Add, Sub, Divide, Multiply"))
    
    if (arithmetic_operation == 'Add'):
        x = float(input("enter your first num"))
        y = float(input("enter second num"))
        print (f"Sum is {x+y}")
    elif (arithmetic_operation == "Sub"):
        x = float(input("enter your first num"))
        y = float(input("enter second num"))
        print (f"Subtraction is {x-y}")
    elif (arithmetic_operation == "Divide"):
        x = float(input("enter your first num"))
        y = float(input("enter second num"))
        print (f"Divide answer is {x/y}")
    elif (arithmetic_operation =="Multiply"):
        x = float(input("enter your first num"))
        y = float(input("enter second num"))
        print (f"Multip is {x*y}")
    else:
        print("We only support Add, Sub, Divide, and Multiply")
        

main()