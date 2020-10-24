def numero_no_indice(*args):
    lista=[]
    i=0
    while i<len(args):
        if args[i]==args.index(args[i]):
            lista.append(args[i])
        i+=1
  
    return lista

