def eh_palindromo(palavra):
    y = palavra[ : : -1]
    
    if palavra == y:
        return True
    else:
        return False