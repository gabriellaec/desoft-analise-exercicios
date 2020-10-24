palavra=input('Palavra:')
lista=[]
if palavra[0]=='A'or'a':
    lista.append(palavra)
else:
    None
while not palavra=='fim':
    palavra=input('Palavra:')
    if palavra[0]=='A'or'a':
    	lista.append(palavra)
	else:
    	None
print(lista)