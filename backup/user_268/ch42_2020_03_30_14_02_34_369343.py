lista=[]
Continue=True
b=0
while Continue:
    a=input("palavra:")
    if a == "fim":
        lista.append(a)
        Continue=False
    else:
        lista.append(a)
p=len(lista)
while b<p:
    if lista[b][0]=="a":
        print (lista[b])
        b+=1
    else:
        b+=1

    