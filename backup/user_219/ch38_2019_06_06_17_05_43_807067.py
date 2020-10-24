def primos_entre(a,b):
    listanaop=[]
    listaprimos=[]
    for i in range(a,b+1):
        lista.append(i)
    for numero in lista:
        for e in range (2,numero):
            if numero%e==0 and e!=x:
                listanaop.append(numero)
            else:
                listaprimos.append(numero)
    contador=0
    for i in listaprimos:
        contador+=1
    return contador
    
                