# 5) Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os
# números primos entre 1 e o número digitado

num = int(input("Digite um número: "))
numbers = []

def listaNumero(num):
    for i in range(1, num + 1):
        numbers.append(i)
    
    return numbers
        
def primo(list):
    lista_primos = []
    for num in list:
        count = 0
        
        for i in range(1, num+1):
            result = num % i
            if result == 0:
                count += 1        
            
        if count == 2:
            print(f"{num} é primo!")
            lista_primos.append(num)

    print(lista_primos)

listaNumero(num)
primo(numbers)