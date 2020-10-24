def numero_no_indice(*x):
    listacerta=[]
    for i in range(0,len(x)):
        if x[i]==x.index(i):
            listacerta.append(x[i])
    print (listacerta)