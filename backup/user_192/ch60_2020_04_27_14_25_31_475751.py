def eh_palindromo(texto):
    if texto[::-1] == texto[:]:
        return True
    else:
        return False