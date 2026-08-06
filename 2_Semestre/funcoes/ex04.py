# 4) Crie uma função que retorna 1 se o aluno for 
# aprovado em uma disciplina e 0 caso contrário, 
# considerando que as seguintes informações são passadas
# como argumentos:

# o número total de aulas de uma disciplina;
# o número de faltas do aluno (que deve ser ≤ 25% das aulas);
# a nota deste aluno (que deve ser ≥ 6).

def student_classification(lessons: int, absences: int, grade: float ):

    if absences <= lessons * 0.25 and grade >= 6:
        return 1
    
    return 0  

print(student_classification(80, 20, 10))