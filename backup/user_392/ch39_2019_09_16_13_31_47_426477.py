soma = 0 
x = True
lista=[]

while x:
    z = int(input('digite números, e zero para: '))
    lista.append(z)
    if z == 0 :
        x = False
for e in lista:
    soma += e

print(soma)

        
    