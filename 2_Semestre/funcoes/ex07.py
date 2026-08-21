def fatorial(num: int):
    if num == 0 or num == 1:
        return 1
    
    if num < 0:
        return "valor inválido"
    
    return num * fatorial(num - 1)

print(fatorial(5))