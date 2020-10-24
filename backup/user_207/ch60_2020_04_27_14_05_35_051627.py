def eh_palindromo (string):
    i= -len(string) +1
    while i<=0:
        rev = +str(string[i])
        i+=1
    if rev == string:
        return True
    else:
        return False