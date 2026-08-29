def soma(arr):
    if len(arr) == 0:
        return 0
    
    first_element = arr[0]
    rest = soma(arr[1:])
    
    return first_element + rest
    
    
arr = [1, 2, 3,4]

print(soma(arr))