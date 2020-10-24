i=1
lista=[]
while i>0:
    a=int(input('digite um numero'))
    lista.append(a)
    if a<=0:
        break
    
print(lista.reverse())