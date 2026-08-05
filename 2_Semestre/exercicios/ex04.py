# 4. Calculadora Simples

# Crie uma função chamada 'calculadora(num1, num2, operacao)' que recebe dois números e uma string
#  indicando a operação ('"+"', '"-"', '"*"' ou '"/"'). A função deve realizar o cálculo correspondente e retornar o resultado.
#  Caso receba uma operação inválida ou uma divisão por zero, trate esse cenário com uma mensagem apropriada.


def calculadora(n1: float, n2: float, op: str):
    try:
        if op == "+":
            return n1 + n2
        
        elif op == "-":
            return n1 - n2

        elif op == "*":
            return n1 * n2

        elif op == "/":
            return n1 / n2
        
    except:
        return "Operação inválida"


print(calculadora(4, 2, "/"))

