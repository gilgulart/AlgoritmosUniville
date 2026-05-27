# 1) Escreva um programa que peça dois números inteiros e imprima todos os
# números inteiros entre eles.

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))

if n1 > n2:
    for i in range(n2 + 1, n1):
        print(i)
else:        
    for i in range(n1 + 1, n2):
        print(i)