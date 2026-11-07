def solicitar_idade():
    while True:
        try:
            idade = int(input('Digite a sua idade: '))
            print(idade)
 
        except Exception as e:
            print(f"")
        