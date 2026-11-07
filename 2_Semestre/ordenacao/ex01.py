arr = [7,2,1,3,8]

new_arr = []

while arr:
    
    minor = arr[0]
    
    for j in range(len(arr)):
        
        if minor > arr[j]:
            minor = arr[j]
    
    new_arr.append(minor)
    arr.remove(minor)
    
print(new_arr)

# print(minor)
    
        