palavra='banana nanica'
dic={}
def conta_bigramas(palavra):
    i=0
    while i<len(palavra)-1:
        key = palavra[i:i+2]
        if key not in dic:
            dic[key] = 0
        dic[key] += 1
        i+=1
	return dic

print(conta_bigramas(palavra))