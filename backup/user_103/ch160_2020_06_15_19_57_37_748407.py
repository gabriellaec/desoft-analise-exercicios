import math
i=0
lista=[]
while i >= 0 and i <= 90:
    math.radians(sinx)= ((4*i)*(180-i))/ ((40500 - i)*(180-i))
    if sinx != (math.sin(math.degrees(i))):
        d= abs(math.sin(i)- sinx)
        lista.append(d)
    i+=1
ang_max = max(lista)
ang_pos = lista.index(ang_max)
print(ang_pos)