nros = int(input ("digite numeros inteiros positivos: "))
nros_lista = []
while nros > 0:
    nros_lista.append(nros)
    nros = int(input ("digite numeros inteiros positivos: "))
    
print (nros_lista)
print (nros_lista[::-1]