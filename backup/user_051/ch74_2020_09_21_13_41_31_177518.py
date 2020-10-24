
def conta_bigramas(b):
    i=0
    q=[]
    while i<len(b)-1:
        c=b[0+i:i+2]
        q.append(c)
        i+=1
    rep = {}
    for item in q:
        if item in rep:
            rep[item] += 1
        else:
            rep[item] = 1
    rep.items()
    return rep
b='banana nanica'
w=conta_bigramas(b)
print(w)