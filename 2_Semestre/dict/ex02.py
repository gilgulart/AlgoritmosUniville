# 2) Escreva um programa que permaneça em laço efetuando a leitura dos seguintes dados:
# número de matrícula, nome do aluno, idade e curso. O número de matrícula é a chave,
# e os demais dados constituem o valor. Faça a leitura desses dados e construa o dicionário
# enquanto não for digitado zero para o número de matrícula.

alunos = {}

while True:
    matricula = int(input("Qual a matricula? "))

    if matricula == 0:
        break

    nome_aluno = str(input("Qual o nome do aluno? "))
    idade = int(input("Qual a idade? "))
    curso = str(input("Qual o curso? "))

    if matricula not in alunos.keys():
        alunos[matricula] = {'nome_aluno': nome_aluno, 'idade': idade, 'curso': curso}

    else:
        print('Matrícula já existe!')

print(alunos)