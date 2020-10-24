palavra=str(input('Palavra:'))
lista=[]
if palavra[0]=='A'or'a':
    lista.append(palavra)
else:
    None
while not palavra=='fim':
    palavra=str(input('Palavra:'))
    if palavra[0]=='A'or'a':
        lista.append(palavra)
    else:
        None
s=len(lista)-1
del lista[s]
print(lista)
