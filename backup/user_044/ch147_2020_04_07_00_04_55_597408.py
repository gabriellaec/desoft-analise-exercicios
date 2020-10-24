def conta_ocorrencias(lista):
    dn={}
    ls=[]
    l=0
    for n in lista:
        ocorrencia=0
        if n in dn:
            l=0   
        else:
            for i in lista:
                if n==i:
                    ocorrencia+=1
            dn[n]=ocorrencia
        
    return dn

def mais_frequente(lista):
    dn=conta_ocorrencias(lista)
    frequente=0
    ls=[]
    for e in dn.values():
        ls.append(int(e))
    p=max(ls)
    maximo=str(p)
    for i in dn:
        if maximo==dn.values():
            frequente=i
    return frequente    
        