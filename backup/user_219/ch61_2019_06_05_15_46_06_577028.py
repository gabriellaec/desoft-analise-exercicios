def eh_palindromo(word):
    if word[::1]== word[::-1]:
        return True
    else:
        return False