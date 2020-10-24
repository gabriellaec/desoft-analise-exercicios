def eh_palindromo(string):
    for e in string:
        if e==len(string)-e:
            return True
        else:
            return False