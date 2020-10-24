running =  True
while running:
    lista=[]
    o=int(input("digite o numero ai"))
    if o != 0:
        lista.append(o)
    else:
        soma=0
        i=0
        while i<len(lista):
            soma+=lista[i]
            i+=1
        running = False
print(soma)
    
    