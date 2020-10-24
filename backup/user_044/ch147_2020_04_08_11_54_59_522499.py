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
    dc=conta_ocorrencias(lista)
    mais=0
    palavra=0
    for i,n in dc.items():
        if n>mais:
            palavra=i
            mais=n
    return palavra
    
    return frequente    
        