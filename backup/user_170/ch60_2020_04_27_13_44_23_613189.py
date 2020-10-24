def eh_palindromo(string):
    p = string[::-1]
    if string == p:
        return True
    else:
        return False