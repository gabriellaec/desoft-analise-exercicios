def conta_bigramas(palavras):
    i=0
    contagem={}
    for palavra in palavras:
        if a[i: :1] in contagem:
            contagem[palavra]+=1
        else:
            contagem[palavra]=1
    i+=1
	return contagem
             
