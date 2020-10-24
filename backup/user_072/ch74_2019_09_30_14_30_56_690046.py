def conta_bigramas(string):
    bigrama=[]
    dicionario={}
   # N=[]
    i=0
    while i<len(string)-1:
        x=string[i]+string[i+1]
        bigrama.append(x)
        n=bigrama.count(bigrama[i])
       # N.append(n)
        dicionario[bigrama[i]] = n
        i+=1
    return dicionario
        
    