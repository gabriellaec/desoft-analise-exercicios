def conta_bigramas(string):
    bigrama=[]
    dicionario={}
    i=0
    while i<len(string)-1:
        x=string[i]+string[i+1]
        bigrama.append(x)
n=bigrama.count(bigrama[i])
dicionario[bigrama[i]]= n
i+=1
return dicionario