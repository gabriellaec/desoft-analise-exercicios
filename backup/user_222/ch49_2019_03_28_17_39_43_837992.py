lista=[]
numero=int(input('numero'))
while numero>0 and numero!=0:
    lista.append(numero)
    numero=int(input('outro numero'))
print(lista[::-1])