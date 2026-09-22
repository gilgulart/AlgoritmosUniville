# 1) Escreva um programa que leia do teclado o código de uma peça e a quantidade
# disponível no estoque. Esses dois dados de entrada são números inteiros. Acrescente o
# par código:quantidade em um dicionário apenas se o código não estiver presente. Caso
# esteja, dê uma mensagem informando essa situação e descarte os dados. O laço termina
# quando for fornecido 0 para o código. Exibir na tela os dados do dicionário, um membro
# por linha

estoque = {}

while True:
    cod = int(input("Qual o código do produto? "))

    if cod == 0:
        break

    qnt = int(input("Qual a quantidade de produto? "))

    try:
        if cod not in estoque:
            estoque[cod] = {
                'quantidade': qnt
            }

            print(f"{cod}: {estoque[cod]}")

        else:
            print('Código já existe!')

    except Exception as e:
        print('Erro: ', e)

print(estoque[cod])
