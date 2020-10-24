def eh_palindromo (palavra):
    if palavra == palavra[::-1]:
        return True
    else:
        return False