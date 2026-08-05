# 8. Fatorial de um Número

# Crie uma função chamada 'fatorial(n)' que recebe um número inteiro não negativo $n$ e calcula o seu fatorial 
# (exemplo: $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$) utilizando uma estrutura de repetição.
# A função deve retornar o resultado.


def fatorial(num: int):
    try:
        if num == 0 or num == 1:
            return 1
        
        return num * fatorial(num - 1)
    except:
        return "Valor inválido"

print(fatorial(2))