def numero_no_indice(lista):
    numero=[]
    for i in range(0,len(lista)):
        if i==lista[i]:
            numero.append(i)
    return (numero)