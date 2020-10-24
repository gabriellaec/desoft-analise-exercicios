def faixa_notas(l):
    l=[]
    i=0
    cinco=0
    cincset=0
    sete=0
    quantidade=[cinco,cinset,sete]
    while(i<len(l)):  
        if(l[i]<5):
            cinco+=1
        elif(l[i]>=5 and l[i]<7):
            cincset+=1
        else:
            sete+=1
    return quantidade
            
            