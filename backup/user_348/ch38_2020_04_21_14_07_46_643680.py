def quantos_uns (numero):
    string = str(numero)
    i = 0
    contador = 0
    while i < len(string):
        if string[i] == '1':
            contador += 1
        i = i + 1
    return contador
     
        