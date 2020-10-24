numeros=[]

novo_numero=int(input("numero: "))

while novo_numero>0:
    numeros.append(novo_numero)
    novo_numero=int(input("numero: "))

a=numeros.reverse()

i=0

while i<len(numeros):
    print(numeros[i])
    i+=1