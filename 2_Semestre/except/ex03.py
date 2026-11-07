def somar_elementos(lista, index_1, index_2):
    try:
        return lista[index_1] + lista[index_2]
   
    except IndexError as e:
        return f'Index out of Range: {e}'
    except TypeError as e:
        return f'Conversão de tipo errada: {e}'    

print(somar_elementos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 'a'))
print(somar_elementos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, 1))