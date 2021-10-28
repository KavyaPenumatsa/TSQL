def large(*args):
    res = args[0]
    for num in args:
        if num > res:
            res = num
    return res
print(large(46,50,23))