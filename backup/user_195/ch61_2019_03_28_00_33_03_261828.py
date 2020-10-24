def eh_palindromo(p):
    i=0
    palindromo=True
    while i<len(p):
        if L[i]!=L[len(p)-1-i]:
        	palindromo=False
        i+=1
    return palindromo