def eh_palindromo(x):
    if x[::1]==x[::-1]:
        return True
    else:
        return False