def eh_palindromo (string):
    for i in string:
        if string[i] == string[-i]:
            return True
        else:
            return False