def conta_bigramas(palavra):
    i=0
    palavra=[]
    contagem={}
    for b in palavra:
        if b in contagem:
            contagem[b]+=1
        else:
            contagem[b]=1
    i+=1
	return contagem
             
