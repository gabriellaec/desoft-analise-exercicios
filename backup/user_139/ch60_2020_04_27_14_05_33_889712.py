def eh_palindromo (frase):
    return frase == frase[::-1]

def eh_palindromo (frase):
    palindromo = True
    i = 0
    j = len(frase) - 1
    while i < j:
        if frase[i] != frase [j]:
            palindromo = False
        i += 1
        j -= 1
    return palindromo