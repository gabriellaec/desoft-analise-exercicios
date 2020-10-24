elemento=int(input('número: '))
lista=[]
x=True
while x:
    elemento=int(input('número: '))
    if elemento > 0:
        lista.append(elemento)
    else:
            x=False
print (lista) 