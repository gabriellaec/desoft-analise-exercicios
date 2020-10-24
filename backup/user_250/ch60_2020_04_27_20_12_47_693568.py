def eh_palindromo(palavra):
    for i in palavra:
        if palavra[i] == palavra[:-i]:
            return True
        else:
            return False