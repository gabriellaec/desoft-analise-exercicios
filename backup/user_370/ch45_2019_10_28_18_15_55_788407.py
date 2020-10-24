def zera_negativos (x):
    i=0
    nova_lista=[]
    cont=0
    while cont < len(x):
        if x[i] < 0:
            x[i]= 0
            nova_lista.append(x[i])
        else:
            nova_lista.append(x[i])
        i+=1
    cont+=1
    return (nova_lista)
        
        