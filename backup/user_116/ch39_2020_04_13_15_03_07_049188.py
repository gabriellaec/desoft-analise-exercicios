i=0
pode=False
lista=[]
while pode==False:
    x=int(input("digite um numero"))
    if x <=1000:
        lista=[x]
        pode=True
while lista[-1]!=1:
    if lista[i]%2==0:
        lista.append(lista[i]/2)
        i+=1
    else:
        lista.append(3*lista[1]+1)
        i+=1
print(lista)
