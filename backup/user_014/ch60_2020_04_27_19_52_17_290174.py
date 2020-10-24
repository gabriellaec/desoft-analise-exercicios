def eh_palindromo(string):
    i = 0
    while i < len(string):
        if string[i] == string[::-1]:
            return True
        else:
            return False
        i += 1