def eh_palindromo(palavra):
    if palavra[-len(palavra):]==palavra[:len(palavra)]:
        palindromo=True
    return palindromo
    