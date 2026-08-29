def lenght(arr):
    if not arr:
        return 0

    count = lenght(arr[1:])
    
    return 1 + count

arr = [1,2,3]
print(lenght(arr))