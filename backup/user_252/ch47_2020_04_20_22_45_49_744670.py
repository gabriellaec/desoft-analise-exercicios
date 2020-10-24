def estritamente_crescente(lista):
    cresce=[]
    i=0
    c=1
    if len(lista)==0:
        return cresce
    else:
        cresce.append(lista[0])
        while c<len(lista):
            y=lista[i]
            x=lista[c]
            if y<x:
                cresce.append(x)
                i=c
                c+=1
            else:
                c+=1
        return cresce