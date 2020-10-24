def separa_trios(x):
    
    lista=[]
    if len(x)>=3:
        for i in range(0,len(x),3):
            lista.append(x[i:i+3])       
    else:
        lista.append(x[::])
    return lista