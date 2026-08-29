def regressive(num):
    if num <= 0:
        return 0
    
    print(num)
    regressive(num - 1)
    
regressive(100)

def count(num):
    if num == 1:
        print(num)
        return
        
    count(num - 1)
    print(num)
    
count(100)

