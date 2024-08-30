class Fruit:
    def __init__(self, name, price, quantity):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.total = price * quantity


apple = Fruit("Apple",3,100)
for x in apple:
    print(x)

# banana = { "name":input("name"), "price":300, "quantity": input("quantity")}

# for x in banana:
#     print(banana[x])

# print(banana['name'])