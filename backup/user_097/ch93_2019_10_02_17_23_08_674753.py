def verifica_numero(numero):

    if(numero < 1):
        return False

    numero_string = str(numero)

    i = 0
    lista_numeros_separados = []
    while (i < len(numero_string)):
        lista_numeros_separados.append(float(numero_string[i]))
        i = i + 1

    i = 0
    verificador = 0
    while (i < len(lista_numeros_separados)):
        verificador = (verificador + (lista_numeros_separados[i]**lista_numeros_separados[i]) )
        i = i + 1

    if(numero==verificador):
       return True
    else:
        return False