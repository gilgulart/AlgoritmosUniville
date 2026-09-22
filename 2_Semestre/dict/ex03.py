# 3) Escreva um programa que permaneça em laço lendo números inteiros do teclado. Esse
# laço termina quando for digitado zero ou qualquer valor negativo. O programa deve
# contar quantas vezes cada valor positivo foi digitado. Ao término do laço de leitura o
# programa deve mostrar quais valores foram digitados e quantas vezes cada um. Use um
# dicionário para resolver esse problema.

numbers = {
    'positive': []}

while True:
    num = int(input("Escreva um numero inteiro: "))

    if num >= 0:
        numbers['positive'].append(num)

    else:
        print(numbers['positive'])
        print('Positivos: ', len(numbers['positive']))
        break

