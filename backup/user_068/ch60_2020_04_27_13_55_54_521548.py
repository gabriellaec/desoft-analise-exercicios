def eh_palindromo(palavra):
    for a in range len(palavra):
        if palavra[a-1] == palavra[-1-a]:
            return True
        else:
            return False
