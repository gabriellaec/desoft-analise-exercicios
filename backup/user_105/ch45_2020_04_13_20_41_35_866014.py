numeros_ordem = []
x = float(input('adicione um numero:   '))
while x >= 1:
	numeros_ordem.append(x)
	x = float(input('adicione um numero:   '))
lista_inversa = []  

i = len(numeros_ordem)
while i!=-1:
	lista_inversa.append(numeros_ordem[i])
	i =  i - 1
print(lista_inversa)