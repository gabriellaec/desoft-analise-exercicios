def conta_bigramas(palavra):
    i=0
    palavra={}
    for b in palavra:
        if b[0: :2] in contagem:
            contagem[b]+=1
        else:
            contagem[b]=1
    i+=1
             
