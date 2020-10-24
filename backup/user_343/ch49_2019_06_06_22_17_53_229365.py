k=True
lista=[]
while k==True:
    n=int(input("N"))
    lista.append(n)
    if n <=0:
        k=False
print (lista[::-1])        