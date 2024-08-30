try:
    print(x)
except NameError:
    print("An error occurred")

except:
    print('something is wrong')
    
finally:
    print("it's done")
    


x = -1
if x<0:
    raise Exception("Sorry, number below zero")