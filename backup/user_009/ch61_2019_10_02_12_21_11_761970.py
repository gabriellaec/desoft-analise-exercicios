def eh_palindromo(x):
    contrario = x[::-1]
    if contrario == x:
        return True
    else:
        return False
    