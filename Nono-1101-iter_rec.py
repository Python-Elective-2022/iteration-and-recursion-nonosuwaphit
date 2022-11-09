base = 0
exp = 0

def iterativePower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp == 1:
        return base
    else:
        return base * (iterativePower(base, exp-1))

print(iterativePower(2,3))