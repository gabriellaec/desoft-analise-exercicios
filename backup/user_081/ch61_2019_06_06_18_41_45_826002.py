
def eh_palindromo(x):
    palindromo = False
    detras = x[0::-1]
    if x == detras:
        palindromo = True
    return palindromo
        
    