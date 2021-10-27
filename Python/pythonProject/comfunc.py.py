def large(x,y,z):
    if x > y and x > z:
        return(x)
    elif y > z and y > x:
        return(y)
    elif z > x and z > y: 
        return(z)
    else:
        print("No number is larger")
x=3
y=5
z=2
print(large(x,y,z))

