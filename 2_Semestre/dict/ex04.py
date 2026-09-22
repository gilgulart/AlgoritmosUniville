# 4) Considere o seguinte conjunto de dados: Nome + (N1, N2, N3, N4). Nome representa o
# nome de um aluno e deve ser usado como chave. N1, N2, N3, N4 representam as notas
# de provas desse aluno. Escreva um programa que leia os dados de Q alunos e apresente
# na tela se foram aprovados ou reprovados. O critério que garante a aprovação é que a
# média aritmética das 4 notas seja maior ou igual 6,0. Q é a quantidade de alunos, e esse
# valor deve ser lido do teclado no começo do programa. As notas devem ser exibidas com
# uma casa decimal

alunos = {}


while True:
    nome = str(input("Qual o nome do aluno? "))

    if nome.lower() == 'fim':
        break

    n1 = int(input("Qual a primeira nota? "))
    n2 = int(input("Qual a segunda nota? "))
    n3 = int(input("Qual a terceira nota? "))
    n4 = int(input("Qual a quarta nota? "))



    if nome in alunos:
        print("Aluno já foi cadastrado!")

    else:
       alunos[nome] = {'notas': [n1, n2, n3, n4]}


for key, value in alunos.items():
    v_media = sum(value['notas']) / len(value['notas'])
    status = 'Aprovado' if v_media >= 6 else 'Reprovado'
    print(f'{key} - {v_media:.2f} ({status})')


print(alunos)