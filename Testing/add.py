def add(x,y):
    if(check_int_float(x) and check_int_float(y)):
        return x+y
    elif():
        return "Error"

def check_int_float(x):
    if(type(x)== int or type(x) == float):
        return True
    else:
        return False
