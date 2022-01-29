a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b**2 -4*a*c

print("delta: ",delta)

kok_1 = (-b - delta ** 0.5) / (2*a)
kok_2 = (-b + delta ** 0.5) / (2*a)

print("Kök 1: {}\nKök 2: {}".format(kok_1,kok_2))