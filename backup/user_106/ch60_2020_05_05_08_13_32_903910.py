def eh_palindromo(string):
    if string==string[::-1]:
        return True
    else:
        return False

def eh_palindromo(string):
    new=[]
    for i in string:
        new.append(i)
    new.reverse()
    news=''.join(new)
    if news==string:
        return True
    else:
        return False