def lista_primos(numero):
    lista = [0]*numero
    contador = 1
    while (contador<numero):
        if (numero%contador==0):
            contador+=1
            if (contador==2):
                lista.append(numero)
             
            
    return (lista)