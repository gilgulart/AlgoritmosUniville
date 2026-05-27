# 4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas
# em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o
# valor -273°C.

celsius = int(input("Digite um valor em celsius: "))
count = 1
totalC = 0

while celsius != -273:
    totalC += celsius
    count += 1
    
    celsius = int(input("Digite um valor em celsius: "))
    
    average = totalC / count
    
print(f'média em celsius: {average},  total em Celsius: {totalC}, contagem: {count}')
    
    