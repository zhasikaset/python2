a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a == b and b == c :
    print("Equilateral triangle")
elif (a==b) or (b==c) or (a==c):
    print("Isosceles triangle")
else:
    print("Scalene triangle")