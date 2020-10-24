def eh_palindromo(x):
    s = x[: : -1]
    if s == x:
        return True
    else:
        return False