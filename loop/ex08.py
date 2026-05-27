# 8) Vamos entender a distribuição de idades de pensionistas de uma empresa de
# previdência. Escreva um programa que leia as idades de uma quantidade não
# informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-
# 75] e [76-100]. Encerre a entrada de dados com um número negativo

age = int(input("informe a idade: "))
count_0a25 = 0
count_26a50 = 0
count_51a75 = 0
count_76a100 = 0

while age >= 0:

    if age >= 0 and age < 26:
        count_0a25 += 1
    elif age > 25 and age < 51:
        count_26a50 += 1
    elif age > 50 and age < 76:
        count_51a75 += 1
    elif age > 75:
        count_76a100 += 1
        
    age = int(input("informe a idade: "))
        
print(f"jovens[0-25]: {count_0a25}, adultos[26-51]: {count_26a50}, idosos[51-75]: {count_51a75}, ancestrais[<76]: {count_76a100} ")    