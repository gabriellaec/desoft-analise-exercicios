def conta_bigramas(palavra):
    i=1
    palavra=[]
    contagem={}
    for b in palavra:
        if b[0: :2] and b!=0 in contagem:
            contagem[b]+=1
        else:
            contagem[b]=1
    i+=1
             
