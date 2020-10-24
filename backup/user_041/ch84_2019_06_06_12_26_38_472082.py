def inverte_dicionario(dic):
    dic={}
    dickeys=[]
    dicvalues=[]
    novodic={}
    i=0
    for k,v in dic:
        dickeys.append(k)
        dicvalues.append(v)
	while i<len(dickeys):
        novodic[dicvalues[i]]=dickeys[i]
        i+=1
    return novodic
        
        
    