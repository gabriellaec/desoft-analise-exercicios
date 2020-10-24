def eh_palindromo(string):
    i = 0
    while i < len(string):
        if string[i] == string[::-i]:
            return True
        else:
            return False
        i += 1