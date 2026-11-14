def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        minor = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[minor]:
                minor = j
        
        arr[i], arr[minor] = arr[minor], arr[i]
        
        return arr
    
numbers = [ 9,23,30,44,14]

# print(selection_sort(numbers))

def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = current
        
        return arr
    
# print(insertion_sort(numbers))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    right = merge_sort(arr[mid:])
    left = merge_sort(arr[:mid])
    
    return merge(left, right)

def merge(left, right):
    result = []
    
    while left and right:
        
        if left[0] < right[0]:
            result.append(left.pop(0))       
        else: 
            result.append(right.pop(0))   
            
    print(result)
    return result + left + right     

print(merge_sort(numbers))