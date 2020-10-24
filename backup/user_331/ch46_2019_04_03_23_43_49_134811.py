lista=[]
i=0
while a!='fim':
	a=str(input('Qual palavra gostaria de adicionar à lista?'))
    lista.append(a)
while i<=len(lista):
    palavra=lista[i]
    if palavra[0]='a':
        print(palavra)
	i+=1