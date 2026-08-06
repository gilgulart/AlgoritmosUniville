# 10. Quantidade de Pares em um Intervalo

# Crie uma função chamada contar_pares(inicio, fim)' que recebe dois inteiros representando
# um intervalo e utiliza um laço de repetição para contar quantos números pares existem dentro desse
# intervalo (incluindo os limites 'inicio' e 'fim'). A função deve retornar essa contagem.


def peer_counter(start: int, stop: int):
    sum = 0
    for i in range (start, stop + 1):
        if i % 2 == 0:
            sum += 1
    return sum

print(peer_counter(1, 10))