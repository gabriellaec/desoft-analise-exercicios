def eh_palindromo(p):
    i=0
    palindromo=True
    while i<len(p):
        a=len(p)-1-i
        if p[i]!=p[a]:
        	palindromo=False
        i+=1
    return palindromo