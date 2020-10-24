def pos_arroba(x):
    x= "usuario@insper.edu.br"
    i=0
    arrobobas = -1
    while i<len(x):
        if x[i]=='@':
        	arrobobas = i
        i+=1
    return arrobobas