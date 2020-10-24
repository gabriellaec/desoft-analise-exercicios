def lista_primos(numero):
    lista = [2, ]
    contador = 1
    divisores = 1
    while (contador<numero):
        contador+=1
        if (numero%contador==0): break
            divisores +=1
        else:
            lista.append(numero)
            
             
    return lista