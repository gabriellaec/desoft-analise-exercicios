def classifica_triangulo(co,ca,h):
    if co==ca==h:
        return 'equilátero'
    elif co==ca or co==h or ca==h:
        return'isósceles'
    else:
        return 'escaleno'
    