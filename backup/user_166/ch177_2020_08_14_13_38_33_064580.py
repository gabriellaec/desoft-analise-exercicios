def numero_digitos(s):
    letras = s.plit()
    digitos=[]
    for letra in letras:
        if letra.isdigit() == True:
            digitos.append(letra)
    return 'há {}'.format(len(digitos)