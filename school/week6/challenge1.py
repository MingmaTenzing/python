
current_room = "Living Room"

while True: 
    print(f"Currently in {current_room}")
    proceed = input("Do you want to proceed to dining room, Yes or No")
    while proceed == "Yes":
        print(f"You are in Dining Room")
        proceed_Further = input("Do you want to go to Kitchen or back to Living Room")
        
        
        if (proceed_Further == "Kitchen"):
            print("You are in Kitchen now")
            print("how ever you can only go back to dining room from here")
            break
            
            
        if(proceed_Further == "Living Room"):
            print("Ok, I'll take you back to Living Room, No worries")
            break
        
    
            
            
    
    
 
    
        