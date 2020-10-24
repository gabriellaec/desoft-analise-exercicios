def numero_no_indice(*x):
    listacerta=[]
    for i in x:
        if x[i]==x.index(i):
            listacerta.append(x[i])
    print (listacerta)