class User:
    def __init__(user, name, age, email):
        user.name = name
        user.age = age
        user.email = email
    
    def __str__(user):
        return f"{user.name}"
    
    def returnDetails(user):
        return {user.name, user.age, user.email}
        

user1 = User("Mingma", 30, "mingma@gmail.com")

print(user1)
print(user1.returnDetails())