def eh_palindromo(texto):
    s = texto[::-1]
    if texto == s:
        return True
    else:
        return False