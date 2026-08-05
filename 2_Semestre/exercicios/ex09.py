# 9. Média de Notas e Situação

# Crie uma função chamada 'verificar_aprovacao(nota1, nota2, nota3)' 
# que calcula a média aritmética de três notas. Com base na média calculada, retorne:

# * **"Aprovado"** se a média for maior ou igual a 7.0.
# * **"Recuperação"** se a média estiver entre 5.0 e 6.9.
# * **"Reprovado"** se a média for menor que 5.0.


def verificar_aprovacao(n1, n2, n3):
    
    media = (n1 + n2 + n3) // 3
    status = "Aprovado" if media >= 7 else "Reprovado" "Recuperação" if media >= 5 and media <= 6.9 else "Reprovado"
    return status

print(verificar_aprovacao(1, 2, 3))
    