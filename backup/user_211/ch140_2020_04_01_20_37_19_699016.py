def faixa_notas(*args):
    l=[]
    cinco=[]
    cincset=[]
    sete=[]
    for i in l:
        if(l[i]<5):
            cinco.append(l[i])
        elif(l[i]>=5 and l[i]<7):
            cincset.append(l[i])
        else:
            sete.append(l[i])
        
    quantidade=(len(cinco),len(cincset),len(sete))
    return quantidade
            
print(faixa_notas(3, 4, 5, 5.5, 6, 9))           