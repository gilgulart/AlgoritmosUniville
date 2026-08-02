# Função que recebe três valores e retorna o maior

def largestValue(v1, v2, v3):
    if v1 >= v2 and v1 >= v3:
        return v1
    elif v2 >= v1 and v2 >= v3:
        return v2
    else:
        return v3

print(largestValue(2, 10, 5))