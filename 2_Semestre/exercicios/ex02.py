# 2. Maior de Dois Números

# Crie uma função chamada 'maior_de_dois(a, b)' que recebe dois números inteiros ou 
# flutuantes e retorna o maior entre eles. Se forem iguais, pode retornar qualquer um dos dois.

def maior_de_dois(a, b):

    if a == b:
        return a or b

    if a > b:
        return a

    return b

print(maior_de_dois(2, 2))
print(maior_de_dois(2, 3))
print(maior_de_dois(2, 1))
