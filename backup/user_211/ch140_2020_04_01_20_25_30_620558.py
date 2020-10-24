def faixa_notas(l):
    l=[]
    i=1
    cinco=0
    cincset=0
    sete=0
    
    while(i<len(l)):  
        if(l[i]<5):
            cinco=cinco+1
        elif(l[i]>=5 and l[i]<7):
            cincset=cincset+1
        else:
            sete=sete+1
        i=i+1
    quantidade=[cinco,cincset,sete]
    return quantidade
            
            