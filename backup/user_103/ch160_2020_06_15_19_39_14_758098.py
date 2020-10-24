import math
i=0
sinx
lista=[]
while i >= 0 and i <= 90:
    sinx= abs(((4*i)*(180-i))/ (40500 - i*(180-i)))
    if sinx != abs(math.sin(i)):
        d= math.sin(i)- sinx
        lista.append(d)
    i+=1

        
ang_max = max (lista)
ang_pos = lista.index(ang_max) 
print(ang_pos)
        