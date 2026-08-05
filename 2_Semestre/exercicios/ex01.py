# 1. Par ou Ímpar

# Crie uma função chamada 'eh_par(numero)' 
# que recebe um número inteiro como parâmetro e retorna 'True' se o número for par e 'False' caso contrário.


def is_peer(num: int):
    if num % 2 == 0:
        return True
    
    return False

print(is_peer(2))
print(is_peer(3))
