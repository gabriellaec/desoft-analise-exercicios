def numero_digitos(qualquer):
    contador = 0
    for i in qualquer:
        if i.isdigit():
            contador +=1
    return contador
