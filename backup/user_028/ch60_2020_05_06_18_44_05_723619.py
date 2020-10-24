def eh_palindromo(palavra):
    if palavra == palavra[::-1]:
        return True
    if palavra != palavra[::-1]:
        return False
    