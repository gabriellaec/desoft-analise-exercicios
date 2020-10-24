def eh_palindromo(string):
    i = 0
    while i < len(string):
        if string[i] == string[::-1]:
            return False
        else:
            return True
        i += 1