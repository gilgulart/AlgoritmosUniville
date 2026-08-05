# 3. Classificação por Idade

# Crie uma função chamada 'classifica_idade(idade)' que recebe a idade de uma pessoa e retorna uma string com a sua categoria:

# * **"Criança"** para idades menores que 12 anos.
# * **"Adolescente"** para idades entre 12 e 17 anos.
# * **"Adulto"** para idades de 18 a 59 anos.
# * **"Idoso"** para idades a partir de 60 anos.

def classifica_idade(idade: int):
    if idade < 12:
        return 'Criança'

    elif idade > 12 and idade <= 17:
        return 'Adolescente'

    elif idade > 18 and idade <= 59:
        return 'Adulto'

    return 'Idoso'

print(classifica_idade(6))
print(classifica_idade(16))
print(classifica_idade(20))
print(classifica_idade(65))
