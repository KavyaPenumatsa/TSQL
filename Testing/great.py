def large(x,y,z):
    if (check_int_float(x) and check_int_float(y) and check_int_float(z)):
        if x > y and x > z:
            return(x)
        elif y > z and y > x:
            return(y)
        elif z > x and z > y:
            return(z)
    else:
        return "Error"

def check_int_float(x):
    if(type(x)== int or type(x) == float):
        return True
    else:
        return False

def check_int_float(y):
    if(type(y)== int or type(y) == float):
        return True
    else:
        return False

def check_int_float(z):
    if (type(z) == int or type(z) == float):
        return True
    else:
        return False

