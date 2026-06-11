# 8) Faça um programa que leia um número indeterminado de notas. Após esta entrada de
# dados, faça o seguinte:
# • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram informadas.
# • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo do outra.
# • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.
# • Calcule e mostre a quantidade de notas acima da média calculada

boletim = []
nota = int(input("informe a sua nota: "))

while nota >= 0:
    if nota > 10:
        nota = int(input("informe um valor válido: "))
        
    boletim.append(nota)
    nota = int(input("informe a sua nota de 0 a 10: "))


qtd_notas = len(boletim)


print(f"Foram lidas {qtd_notas} notas \n")
print(f"As notas foram informadas nesta ordem: {boletim}")

for i in range(len(boletim), 0, -1):
    print(boletim[i - 1])
    
    