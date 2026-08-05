# 7. Verificador de Múltiplos

# Crie uma função chamada 'eh_multiplo(a, b)' que recebe dois inteiros e retorna 'True' se $a$
# for múltiplo de $b$ 
# (ou seja, se a divisão de $a$ por $b$ tiver resto zero) e 'False' caso contrário.

def is_multiple(num: int, multiple: int):
    if num % multiple == 0:
        return True
    
    return False

print(is_multiple(3, 2))
print(is_multiple(4, 2))