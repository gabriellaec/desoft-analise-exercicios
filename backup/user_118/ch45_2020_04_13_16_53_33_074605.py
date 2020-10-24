i=0
lista=[]
listar_numeros=True
while listar_numeros:
    numero=inr(input('Diga um número inteiro: '))
    i+=1
    if numero>0:
        lista.append(numero)
    else:
        listar_numeros=False
print (lista[::-1])