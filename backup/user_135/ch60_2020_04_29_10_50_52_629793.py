def eh_palindromo(texto):
    texto_invertido = texto[::-1]
    if texto_invertido == texto:
        return True
    else:
        return False