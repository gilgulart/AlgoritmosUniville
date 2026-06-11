# 7) Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas
# respostas. Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se
# a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C
# ou D.
# Gabarito da prova:
# 01 - D
# 02 - A
# 03 - C
# 04 - B
# 05 - A
# 06 - D
# 07 - C
# 08 - C
# 09 - A
# 10 – B

template = ['d', 'a', 'c', 'b', 'a', 'd', 'c', 'c', 'a', 'b']
answers = []

for i in range(10):
    answer = str(input(f"informe a resposta da questão {i+1}: ")).lower()
    answers.append(answer)
    
nota = 0
    
for i in range(10):
    if answers[i] == template[i]:
        nota += 1
                  
        
        
print("nota final: ",nota)  
print(answers)