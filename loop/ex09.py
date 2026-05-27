# 9) Em uma eleição para gerência em uma empresa com 20 pessoas
# colaboradoras, existem quatro candidatos(as). Escreva um programa que calcule
# o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:

# • Cada colaborador(a) votou em uma das quatro pessoas candidatas (que
# representamos pelos números 1, 2, 3 e 4).

# • Também foram contabilizados os votos nulos (representados pelo número
# 5) e os votos em branco (representados pelo número 6).

# Ao final da votação, o programa deve exibir o número total de votos para cada
# candidato(a), os nulos e os votos em branco. Além disso, deve calcular e exibir a
# porcentagem de votos nulos em relação ao total de votos e a porcentagem de
# votos em branco em relação ao total de votos.

urna = [1, 2, 3, 4, 5, 6]
zezinho = 0
madruga = 0
maurilio = 0
betao = 0
branco = 0
nulo = 0

for i in range(20):
    vote = int(input("""
                     1- Zézinho
                     2- Madruga
                     3- Maurílio
                     4- Betão
                     5- Votar Branco
                     6- Votar Nulo
                     """))
    while vote not in urna:
        print("vote em um candidato válido...")
        vote = int(input("""
                     1- Zézinho
                     2- Madruga
                     3- Maurílio
                     4- Betão
                     5- Votar Branco
                     6- Votar Nulo
                     """))
    if vote ==  1:
        zezinho += 1
        
    elif vote == 2:
        madruga += 1
        
    elif vote == 3:
        maurilio += 1
        
    elif vote == 4:
        betao += 1
    
    elif vote == 5:
        branco += 1
        
    elif vote == 6:
        nulo += 1
        
print(f"Zezinho: {zezinho}, Madruga: {madruga}, Maurílio: {maurilio}, Betão: {betao}, Brancos: {branco}, Nulo: {nulo} ")  
print(f"Zezinho: {(zezinho / 20) * 100}%, Madruga: {(madruga / 20) * 100}%, Maurílio: {(maurilio / 20) * 100}%, Betão: {(betao / 20) * 100}%, Brancos: {(branco / 20) * 100}%, Nulo: {(nulo / 20) * 100}%")   
    
        