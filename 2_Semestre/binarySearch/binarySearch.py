def binary_search(list, item):
    left = 0
    right = len(list) - 1
    
    while left <= right:
        middle = (left + right) // 2
        guess = list[middle]
        
        if guess == item:
            return middle
        
        if guess > item:
            right =  middle - 1
        
        else:
            left = middle + 1
    
    return None


ordered = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
impar = [1, 3, 5, 7, 9, 11, 13, 15, 17]
par = [2, 4, 6, 8, 10, 12, 14, 16, 18] 

print (binary_search(ordered, 15))
print (binary_search(impar, 15))
print (binary_search(par, 12))