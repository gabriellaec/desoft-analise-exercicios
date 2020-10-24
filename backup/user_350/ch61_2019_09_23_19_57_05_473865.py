def eh_palindromo(n):
    if n[::1]==n[::-1]:
        return True
    return False