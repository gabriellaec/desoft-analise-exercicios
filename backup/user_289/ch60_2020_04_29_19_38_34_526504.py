def eh_palindromo(string):
    A = str(string)
    B = A[::-1]
    if A == B:
        return True
    else:
        return False