import random
print("HOW MANY WORDS?")
a = int(input(""))
print("WRITE YOUR WORDS AND USE SPACE")
b = input("").split()
d = random.randrange(0, a+1)
print(b[d])
