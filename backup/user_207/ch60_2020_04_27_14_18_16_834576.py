def eh_palindromo (string):
    i=-1
    rev = string[i]
    while i>len(string):
        add = string[i]
        rev += add
        i-=1
    if rev == string:
        return True
    else:
        return False