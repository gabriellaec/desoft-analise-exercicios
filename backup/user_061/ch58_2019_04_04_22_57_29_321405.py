def calcula_fibonacci(numero):
    if numero == 0:
        lista = [1]
    elif numero == 1:
        lista = [1,1]
    else:
        lista = [0]*2
        lista[0]=1
        lista[1]=1
        i = 1
        while i < numero:
            lista.append(lista[i]+lista[i-1])
            i+=1
    return lista