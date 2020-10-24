running =  True
while running:
    lista=[]
    o=int(input("digite o numero ai"))
    if o != 0:
        lista.append(o)
    else:
        soma=0
        for i in lista:
            soma+=i
        running = False
        
print(soma)
    
    