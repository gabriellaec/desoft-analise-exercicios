running = True
lista=[]
lista2=[]
while running:
    lista.append(float(input("numero")))
    if lista[-1]<=0:
        i=len(lista)
        while i>0:
            lista2.append(lista[i-1])
            i-=1
        running = False
            
        
    