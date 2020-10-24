def verifica_lista(lista):
    i=0
    par=[]
    impar=[]
    if len(lista)==0:
        return "misturado"
    while i<len(lista):
        if i%2==0:
            par.append(i)
            i+=1
        else:
            impar.append(i)
            i+=1
    if len(par)==0 and len(impar)>0:
        return "ímpar"
    elif len(par)>0 and len(impar)==0:
        return "par"
    elif len(par)>0 and len(impar)>0:
        return "misturado"