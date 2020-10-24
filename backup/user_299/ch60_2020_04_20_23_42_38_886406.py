def eh_palindromo(string):
    for i,letra in enumerate(string):
        if string[i] == string[-i]:
            return True
        else:
            return False