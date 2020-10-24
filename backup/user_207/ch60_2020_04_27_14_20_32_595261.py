
def eh_palindromo (string):
    i=-1
    rev = string[i]
    while i>-len(string):
        i-=1
        add = string[i]
        rev += add
    if rev == string:
        return True
    else:
        return False