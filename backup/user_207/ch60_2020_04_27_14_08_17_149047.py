def eh_palindromo (string):
    
    rev = string[-1]
    i= -len(string) +2
    while i<=0:
        add = string[i]
        rev += add
        i+=1
    if rev == string:
        return True
    else:
        return False