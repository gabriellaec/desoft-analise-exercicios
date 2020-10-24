def eh_palindromo(string):
    palavra = str(string)
    palavra2 = palavra[::-1]
    if palavra == palavra2:
        return True