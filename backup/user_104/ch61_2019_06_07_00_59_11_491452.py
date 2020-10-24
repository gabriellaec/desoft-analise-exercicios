def eh_palindromo(palavra):
    t = palavra[ : : -1]
    if palavra == t:
        palindromo = True
    elif palavra != t:
        palindromo = False
    return palindromo    