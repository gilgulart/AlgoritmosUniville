def division(num, num2):
    try:
        return num / num2
    
    except Exception as e:
        return f"{e}"
    
print(division(10, 0))
print(division(10, "10"))