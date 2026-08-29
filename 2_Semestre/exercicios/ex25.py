arr = [2, 4, 5, 6, 8, 10,15,45,30]

def count_peer(arr):
    

    if len(arr) == 0:
        return 0
    
    rest = count_peer(arr[1:])
    
    if arr[0] % 2 == 0:
        return rest + 1
        
    else:
        return rest
    
    

print(count_peer(arr))   