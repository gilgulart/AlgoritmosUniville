# 2) Escreva um programa para calcular quantos dias levará para a colônia de uma
# bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas
# de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia
# com 4 elementos e a B com 10.

colonia_A = 4
colonia_B = 10
dias = 0

while colonia_A < colonia_B:
    
    dias += 1
    
    colonia_A += colonia_A * 0.03
    colonia_B += colonia_B * 0.015

print(f"{dias} dias para igualar e {dias + 1} para ultrapassar")