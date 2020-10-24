lista = []

p = input("Digite uma palavra: ")
lista.append(p)
while p != "fim":
    p = input("Digite uma palavra: ")
    lista.append(p)

i=0
while i < len(lista): 
	if lista[i][0] == a:
        print lista[i]
     i=i+1