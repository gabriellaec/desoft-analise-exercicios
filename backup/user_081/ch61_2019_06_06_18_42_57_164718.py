
def eh_palindromo(x):
    palindromo = False
    detras = x[0::-1]
    for i in range(0,len(x)+1):
        if  i == " ":
            del i 
    		if x == detras:
        		palindromo = True
    return palindromo
        
    