def eh_palindromo(frase):
    for letra in frase:
        if frase[0:len(frase)] == frase[::-1]:
            return True 
    return False