while True:
    try:
        num = int(input('Digite um número inteiro: '))
        print(num)
        exit()
    except Exception as e:
        print(type(e), "Entrada inválida, digite apenas números")
        
        