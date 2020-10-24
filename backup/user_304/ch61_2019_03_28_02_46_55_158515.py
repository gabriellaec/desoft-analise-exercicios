def eh_palindromo (palavra):
    eh_palindromo = True
    if palavra [::-1]!=palavra:
        eh_palindromo = False
    return eh_palindromo 