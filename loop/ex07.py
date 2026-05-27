# 7) Os números primos possuem várias aplicações dentro da Ciência de Dados em
# criptografia e segurança, por exemplo. Um número primo é aquele que é divisível
# apenas por um e por ele mesmo. Assim, faça um programa que peça um número
# inteiro e determine se ele é ou não um número primo.

num = int(input("informe um número: "))
count = 0

for i in range (1, num+1):
    result = num % i
    if num % i == 0:
        print(f"{num} % {i} = {result}")
        count += 1        
    
        
if count == 2:
    print("é primo!")
    
else:
    print("não é primo!")        
    
    
    
    