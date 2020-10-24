#def eh_palindromo(x):
#    return x == x[ : : -1]

def eh_palindromo(x):
    y = ""
    i = len(x)
    while i>0:
        y += x[i-1]
        i = i-1
    return x==y