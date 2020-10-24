def numero_no_indice(*args):
    lista=[]
    for i in args:
        if i==args.index(i):
            lista.append(i)
    print (lista)