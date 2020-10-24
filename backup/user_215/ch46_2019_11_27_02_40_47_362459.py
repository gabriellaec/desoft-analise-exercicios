palavra = input("Insira uma palavra: ")
lista = []

while palavra != "fim":
    lista.append(palavra)
    palavra = input("Insira uma palavra: ")
    
for i in lista:
    if i[0] == "a":
        print(lista[i])
	i += 1        
