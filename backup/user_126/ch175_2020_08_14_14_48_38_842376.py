def imprime_tabuada (n):
    lista=[]
    for i in range (n):
        b=i+1
        lista.append(b)
        y=b
        for ii in range (n-1):
            y+=b
            lista.append(y)
    print (lista)
