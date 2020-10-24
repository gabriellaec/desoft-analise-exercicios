def collatz(numero):
    lista=[]
    while numero != 1:
        if numero % 2 == 0:
            numero= numero/2
            lista.append(numero)
        elif numero % 2 != 0:
            numero= 3*numero + 1
            lista.append(numero)
        
    return len(lista)

acumulador=0
for k in range(1,1000):
    if collatz(k)>acumulador:
        acumlador=collatz(k)
        g=k

print(g)