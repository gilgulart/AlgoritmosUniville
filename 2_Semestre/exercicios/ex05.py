# 5. Contagem Regressiva

# Crie uma função chamada 'contagem_regressiva(inicio)' que recebe um número inteiro positivo e imprime na tela
#  uma contagem regressiva a partir dele até o número **0**, utilizando uma estrutura de repetição ('while' ou 'for').

def contagem_regressiva(inicio: float):
    for i in range(inicio, 0, -1):
        print(i)

contagem_regressiva(100)