f = open("demo.txt", "a")

f.write("Now the file has more contnet")
f.close()

f = open("demo.txt", "r")
print(f.read())

