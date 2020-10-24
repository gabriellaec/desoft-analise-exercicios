lista=[0]
contador=0
a=True
while a==True:
    if lista[contador] == ("fim"):
        a=False
    else:
        lista.append(str(input("elementos ")))
        contador+=1
del lista[0]
i=0
b=len(lista)
while i<b:
    if lista[i][:1] !=("a"):
        del lista[i]
        b=len(lista)
    else:
        i+=1
p=0
while p<b:
    print(lista[p])
    p+=1
