def eh_palindromo(string):
    for e in string:
        if string[e]==len(string)-e:
            return True
        else:
            return False