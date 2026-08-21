def decompose(num: int):
    if num <= 9:
        print(num)
    
    else: 
        decompose(num // 10)
        print(num % 10)
        
decompose(3214)