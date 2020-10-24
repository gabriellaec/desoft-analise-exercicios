with open('churras.txt') as arq:
    
    cont = arq.read()
lista = cont.split(\n)

p = 0

for i in lista:
    
    new = i.split(',')
    w = float(new[1])
    o = float(new[2])
    p+= w*o
print(p)