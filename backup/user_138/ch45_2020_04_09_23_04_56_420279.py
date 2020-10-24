lista=[]
numero=int(input('Qual o número?'))
while numero>0:
    lista.append(numero)
    numero=int(input('Qual o número?'))
print (lista[::-1])
            