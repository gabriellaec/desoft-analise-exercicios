lista=[]
x=0
while len(lista)==100:
    lista.append(1/2**x)
    x+=1
soma=sum(lista)
print (soma)
