def numero_digitos(s):
    letras = s.plit()
    digitos=[]
    for letra in letras:
        if letra in digitos == False:
            if letra.isdigit() == True:
                digitos.append(letra)
    return 'há {} dígitos:{}'.format(len(digitos),digitos)