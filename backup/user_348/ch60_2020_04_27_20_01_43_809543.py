def eh_palindromo (string):
    for i in range(string):
        if string[i] == string[::-i]:
            return True
        else:
            return False