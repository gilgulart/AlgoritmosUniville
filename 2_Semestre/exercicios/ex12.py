def is_palindrome(word: str):
    if len(word) <= 1:
        return True
    
    if word[-1] == word [0]:
        is_palindrome(word[1:-1])
        return True

    return False

print(is_palindrome("ana"))