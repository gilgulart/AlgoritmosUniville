def sum_n(num):
    if num == 1:
        return 1
    
    return num + sum_n(num - 1)
    

print(sum_n(5))