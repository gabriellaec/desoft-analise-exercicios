def verifica_numero(numero):
    i = 0 
    resultado = 0 
    operador = str(numero)
    while i < len(operador):
        resultado += (int(operador[i]))**(int(operador[i]))
        i+=1
    if numero < 1:
        return False
    elif numero != resultado:
        return False
    else: 
        return True