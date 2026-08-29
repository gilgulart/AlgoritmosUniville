def maximo(arr):
    if len(arr) == 1:
        return arr[0]
    
    guess = maximo(arr[1:])
    
    if arr[0] > guess:
        return arr[0]
    else:
        return guess
            

arr = [1,2,3,5,10]

print(maximo(arr))