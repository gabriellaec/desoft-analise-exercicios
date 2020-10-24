def eh_palindromo(string):
    i = 0
    z = -1
    while i < len(string):
        if string[i] == string[::z]:
            return True
        else:
            return False
        i += 1
        z -= 1