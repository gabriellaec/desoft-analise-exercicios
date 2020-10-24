def numero_no_indice(*x):
    listacerta=[]
    i=0
    while(i<len(x)):
        if x[i]==x.index(i):
            listacerta.append(x[i])
        i+=1
    print (listacerta)