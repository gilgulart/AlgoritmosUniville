# 5. Contagem Regressiva

# Crie uma função chamada 'contagem_regressiva(inicio)' que recebe um número inteiro positivo e imprime na tela
#  uma contagem regressiva a partir dele até o número **0**, utilizando uma estrutura de repetição ('while' ou 'for').

def contagem_regressiva(i: int):
    print(i)
    if i <= 1: 
        return
    contagem_regressiva(i - 1)
    
contagem_regressiva(100)