def pot(base: int, exponent: int):
    if exponent == 1:
        return base
    
    if exponent == 0:
        return 1
    
    result = pot(base, exponent - 1)
    
    return base * result

print(pot(2,4))    
    
    
    
    