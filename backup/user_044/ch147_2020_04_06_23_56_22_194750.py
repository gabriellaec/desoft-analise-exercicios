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
    dn=conta_ocorrencia(lista)
    x=max(dn.values())
    for i in (len(dn)):
        if x==dn.values():
            frequente=dn[i]
    return frequente    
        