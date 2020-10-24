def numero_digitos(s):
    letras = s.plit()
    digitos=[]
    for letra in letras:
        if letra not in digitos:
            if letra.isdigit() == True:
                digitos.append(letra)
    return 'há {} digitos:{}'.format(len(digitos),digitos)