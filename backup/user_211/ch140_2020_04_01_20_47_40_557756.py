def faixa_notas(*args):
    l=[*args]
    cinco=[]
    cincset=[]
    sete=[]
    i=1
    while(i<len(l)):
        if(l[i]<5):
            cinco.append(l[i])
        elif(l[i]>=5 and l[i]<7):
            cincset.append(l[i])
        else:
            sete.append(l[i])
        i=i+1
    quantidade=[len(cinco),len(cincset),len(sete)]
    return quantidade
                      