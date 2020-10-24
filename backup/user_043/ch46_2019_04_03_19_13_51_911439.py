palavra=input('Palavra: ')
lista=[]

while palavra!='fim':
    lista.append(palavra)
    palavra=input('Palavra: ')
i=0
while i<len(lista):
    if len(palavra)>1 and palavra[0]=='a':
        print(lista[i])
	