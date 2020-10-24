def eh_palindromo(a):
    if a[0:len(a)] == a[len(a):0]:
        return True
    return False