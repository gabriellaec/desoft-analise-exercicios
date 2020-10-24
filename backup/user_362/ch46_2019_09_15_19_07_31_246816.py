lista=[]
palavra=input("Digite uma palavra: ")
while palavra!="fim":
    lista.append(palavra)
    palavra=input("Digite uma palavra: ")
	
i=0
while i < len(lista):
    palavra = lista[i]
    if len(palavra) > 1 and palavra[0] == 'a':
        print(palavra)
    i += 1