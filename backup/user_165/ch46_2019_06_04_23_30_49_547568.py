lista = []
x = input("Digite uma palavra: ")
while x!= "fim":
    print('Adicionado na lista')
    x = input("Digite uma palavra: ")
    lista.append(x)
for palavra, i in lista:
	palavra = lista[i]
	letra = palavra[0]
	if letra == 'a':
		print(palavra)
    
    