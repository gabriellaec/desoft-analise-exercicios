lista = []
x = input("Digite uma palavra: ")
if x!= "fim":
	lista.append(x)
while x!= "fim":
    print('Adicionado na lista')
    x = input("Digite uma palavra: ")
    lista.append(x)
i=0
while i<len(lista):
    palavra=lista[i]
    letra = palavra[0]
    if letra == 'a':
        print (palavra)
    i+=1
        