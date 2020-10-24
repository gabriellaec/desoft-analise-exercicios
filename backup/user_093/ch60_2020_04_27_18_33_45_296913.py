def eh_palindromo(x):
    a= x[::-1]
    b= x[:]
    if a==b:
        return True
    else:
        return False