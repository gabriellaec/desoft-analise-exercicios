def conta_bigramas(b):
    i=0
    lista=[]
    while i<len(b)-1:
        c=b[0+i:i+2]
        lista.append(c)
        i+=1
    return lista
b='banana nanica'
q=conta_bigramas(b)
def acha_bigramas(q): 
    rep = {}
    for item in q: 
        if (item in rep): 
            rep[item] += 1
        else: 
            rep[item] = 1
    rep.items() 
    print (rep)
if __name__ == "__main__":  
    acha_bigramas(q)