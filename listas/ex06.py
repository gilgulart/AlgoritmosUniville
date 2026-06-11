# 6) Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por
# números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são
# amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de
# produtos doces e amargos.

sweet = []
bitter = []

for i in range(10):
    id = int(input('informe um id: '))
    if id % 2 == 0:
        sweet.append(id)
    else:
        bitter.append(id)
        
print(f"lista de id doce: {sweet}, quantidade de doces: {len(sweet)}")
print(f"lista de id amargo: {bitter}, quantidade de amargos: {len(bitter)}")