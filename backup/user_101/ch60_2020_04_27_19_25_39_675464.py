def eh_palindromo(s):
    p = s[::-1]
    if p == s:
        return True
    else:
        return False