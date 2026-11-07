def busca_menor(arr = []) -> int:
    menor = arr[0]
    menor_indice = 0
    
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
            
    return menor_indice
    

print(busca_menor([9,7,2,1,3]))

def ordena_lista(arr = []) -> list:
    novoArr = []
    
    for i in range(len(arr)):
        menor = busca_menor(arr)
        novoArr.append(arr.pop(menor))
        
    return novoArr

print(ordena_lista([9,7,2,1,3]))
