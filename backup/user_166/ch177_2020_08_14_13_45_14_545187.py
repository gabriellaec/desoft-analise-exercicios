def numero_digitos(s):
    letras = s.plit()
    digitos=[]
    for letra in letras:
        if letra in digitos == False:
            if letra.isdigit() == True:
                digitos.append(letra)
    return len(digitos)
#comecei a prova 10h05 e só consegui fazer até 10h40 pois tenho médico marcado 11h15  