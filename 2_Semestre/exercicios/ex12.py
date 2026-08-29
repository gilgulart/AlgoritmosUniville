def is_palindrome(phrase: str):
    phrase = phrase.lower()
    
    if len(phrase) <= 1:
            return True
        
    elif phrase[0] == phrase[-1]:
       status = is_palindrome(phrase[1:-1])
       return status

    return False

phrase = input("Informe uma frase e verifique se é palíndromo: ")

print("É palíndromo" if is_palindrome(phrase) else "Não é palíndromo")



