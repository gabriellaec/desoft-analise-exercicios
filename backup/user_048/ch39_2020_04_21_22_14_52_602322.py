lista=[]
liste=[]
for e in range(1,1001):
    n=e
    o=0
    lista.append(e)
    while n!=1:
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
        o+=1
    liste.append(o)
    x=dict(zip(lista,liste))
    y=max(liste)
for chave,valor in x.items():
    if valor==y:
        print(chave)
        