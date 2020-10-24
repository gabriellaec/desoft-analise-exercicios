def eh_palindromo(palavra):
    for a in palavra:
        if palavra[a] == palavra[-1-a]:
            return True
        else:
            return False
