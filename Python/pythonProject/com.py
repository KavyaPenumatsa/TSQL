x = int(input("enter x"))
y = int(input("enter y"))
z = int(input("enter z"))
if x>y and x>z:
    print(x)
elif y>z and y>x:
    print(y)
elif z>x and z>y:
    print(z)
else:
    print("No number is larger")



