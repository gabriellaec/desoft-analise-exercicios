import math
lista_seno = []
lista_python = []
nova_lista = []
for i in range (0,91):
    senox = (4*i*(180-i))/(40500-i*(180-i))
    python_seno = math.sin(math.radians(i))
    lista_seno.append(senox)
    lista_python.append(python_seno)
for i in range (0,91):
    nova_lista.append(abs(lista_python[i]-lista_seno[i]))
    
print (nova_lista.index(max(nova_lista)))