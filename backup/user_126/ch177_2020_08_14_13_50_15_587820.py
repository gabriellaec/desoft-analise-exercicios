def numero_digitos(palavra):
    contador=0
    for i in range (len(palavra)):
        if palavra[i].isdigit()==True:
            contador+=1
    return contador   

