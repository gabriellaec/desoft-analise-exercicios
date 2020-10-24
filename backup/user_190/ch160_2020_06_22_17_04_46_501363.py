import math
lista_seno = []
lista_senop = []
nova = []
for i in range (0, 91):
    senox = (4*i*(180-i))/(40500 - i*(180-i))
    senop = math.sin(math.radians(i))
    lista_seno.append(senox)
    lista_senop.append(senop)
for i in range (0, 91):
    nova.append(abs(lista_senop[i]-lista_seno[i]))
    
print (nova.index(max(nova)))                