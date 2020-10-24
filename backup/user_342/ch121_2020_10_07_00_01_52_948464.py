def subtracao_de_listas(x,y):
    a=0
    diferentes=[]
    while a< len(x):
        if x[a] not in y:
            diferentes.append(x[a])
        a=a+1
    return diferentes
    
    