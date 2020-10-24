def eh_palindromo(frase):
    letras = frase.split()
    if letras[::-1] == letras[: :1]:
        return True
    
