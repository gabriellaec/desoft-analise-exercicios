def eh_palindromo(string):
    contador = True
    e = 0
    for e in len(string):
        if string[e]==len(string)-e:
            return True
        else:
            return False