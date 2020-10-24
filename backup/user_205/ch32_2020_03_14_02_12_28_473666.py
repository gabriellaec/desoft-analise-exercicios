def lista_primos(numero):
    lista = [2, ]
    contador = 1
    divisores = 1
    while (contador<numero):
        contador+=1
        if (numero%contador==0): 
            divisores +=1
            if (divisores==2):
                  lista.append(numero)
                
        else:
            break
            
             
    return lista