def mdc(x: int, y: int):
    if y == 0:
        return x
    
    return mdc(y, x % y)    
    
    
print(mdc(75, 30))