elemento=int(input('número: '))
i=0
lista=[]
x=True
while x:
    elemento=int(input('número: '))
    i+=1
    if elemento > 0:
        lista.append(elemento)
    else:
            x=False
print (lista[::-1]) 