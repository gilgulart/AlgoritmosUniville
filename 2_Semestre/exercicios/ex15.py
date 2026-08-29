def busca_menor(arr):
    menor = arr[0]
    menor_indice = 0
    
    for i in range(0, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
        
    return menor_indice

array = [-1,2,3,4,5,6,82,0,65,34,23,54,33,56,55,87]

print(busca_menor(array))

def selection_order(arr):
    new_arr = []
    for i in range(len(arr)):
        menor = busca_menor(arr)
        new_arr.append(arr.pop(menor))
        
    return new_arr

print(selection_order(array))