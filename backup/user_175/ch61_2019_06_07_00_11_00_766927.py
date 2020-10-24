def eh_palindromo(x):
    i = 0
    while i < len(x):
        if x[i] == x[len(x)-(1+i)]:
        	i += 1
        else:
            return False
    return True