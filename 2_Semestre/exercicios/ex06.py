# 6. Soma de 1 a N

# Crie uma função chamada 'soma_ate_n(n)' que recebe um número inteiro positivo $n$ e calcula a soma de todos os 
# números inteiros de 1 até $n$ 
# utilizando um laço de repetição. A função deve retornar o total somado

def  soma_ate_n(n):
    if n < 0:
        return "Apenas valores positivos serão válidos"
    
    sum = 0
    
    for i in range(1,n + 1):
      sum += i
    
    return sum
        
print(soma_ate_n(2))