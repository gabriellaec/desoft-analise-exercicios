def numero_no_indice(n):
    listacerta=[]
    for i in range(0,len(n)):
        if n[i]==n.index[i]:
            listacerta.append(n[i])
    print (listacerta)