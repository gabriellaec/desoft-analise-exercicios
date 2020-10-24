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
    frequente='oi'
    ls=[]
    for e in dn.values():
        ls.append(int(e))
    p=max(ls)
    maximo=str(p)
    for i in dn:
        if dn[i]==maximo:
            frequente=i
    
    return frequente    
        