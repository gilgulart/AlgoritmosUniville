# Função para encotrar o perímetro do triângulo

def perimeter(a, b, c):
    perimeter =  a + b + c
    return perimeter

ladoA = float(input("Informe o lado do triângulo A: "))
ladoB = float(input("Informe o lado do triângulo B: "))
ladoC = float(input("Informe o lado do triângulo C: "))

perimetro = perimeter(ladoA, ladoB, ladoC)

print(perimetro)