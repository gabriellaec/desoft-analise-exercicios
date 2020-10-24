lista=[]
i = 1
numeros=int(input("Digite um numero: "))
while numeros > 0:
	lista.append(numeros)
	numeros=float(input("Digite um numero: ")


lista_in=[]
while i <=len(lista):
	lista_in.append(lista[(len(lista)-i)])                 
	i+=1
print(lista_in)                  