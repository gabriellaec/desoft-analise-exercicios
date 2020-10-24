def eh_palindromo(string):
    return string[:] == string[::-1]
"""def eh_palindromo(string):
    inverso = ''
    for i in range(len(string)-1, -1, -1):
        inverso+=string[i]
    if inverso == string:
        return True
    else:
        return False
"""
"""
def eh_palindromo(string):
    if string[:] == string[::-1]:
        return True
    return False
    """