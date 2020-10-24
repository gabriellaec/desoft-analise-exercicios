def eh_palindromo(string):
    for e in len(string):
        if string[e]==len(string)-e:
            return True
        else:
            return False