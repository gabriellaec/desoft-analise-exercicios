lista=[]
i=0
while a!='fim':
	a=input('Qual palavra gostaria de adicionar à lista?')
    lista.append(a)
while i<len(lista):
    if lista[i]:
        print(lista[i]