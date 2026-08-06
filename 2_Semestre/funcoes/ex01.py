# Função que recebe três valores e retorna o maior

def greatest_value(v1, v2, v3):
    if v1 >= v2 and v1 >= v3:
        return v1
    elif v2 >= v1 and v2 >= v3:
        return v2
    
    return v3

print(greatest_value(2, 10, 5))