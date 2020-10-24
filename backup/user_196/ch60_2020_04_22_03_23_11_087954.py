def eh_palindromo(frase):
    palavras = frase.split()
    junto = "".join(palavras)
    inverso = ""
    for letra in range(len(junto)-1, -1, -1):
        inverso+=junto[letra]
    if inverso == junto:
        return True
    else:
        return False