def notaConceito(nota):
    
    if nota >= 9 and nota <= 10:
        return "A"
    elif nota >= 8 and nota < 9:
        return "B"
    elif nota >= 7 and nota < 8:
        return "C"
    elif nota >= 6 and nota < 7:
        return "D"
    
    return "F"

print(notaConceito(3))
print(notaConceito(9))
print(notaConceito(7))
print(notaConceito(6))
print(notaConceito(5))