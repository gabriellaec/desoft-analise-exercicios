def quantos_uns(x):
    x = str(x)
    contador = 0 
    for i in range(0,len(x)):
        if x[i] == '1':
            contador +=1
    return contador
         