def verifica_numero(n):
    lista_n = []
    i = 0
    num = str(n)
    numero = 0
    numero_string = ''
    while i<len(str(n)):
        lista_n.append(num[i])
        i+=1
    for x in lista_n:
        numero = numero + int(x)**int(x)
    for z in lista_n:
        numero_string = numero_string + z
    if n < 1:
        return False
    elif numero == int(numero_string):
        return True
    else:
        return False