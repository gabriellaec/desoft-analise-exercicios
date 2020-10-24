def conta_bigramas(palavra):
    i=0
    bigrama=[]
    contagem={}
    for bigrama in palavra:
        if bigrama[0: :1] in contagem:
            contagem[bigrama]+=1
        else:
            contagem[bigrama]=1
    i+=1
	return contagem
             
