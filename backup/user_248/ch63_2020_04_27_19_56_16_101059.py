def nome_usuario(x):
    i=0
    while i<len(x):
        if x[i]=='@':
            return (x[0:i])
        else:
            i+=1