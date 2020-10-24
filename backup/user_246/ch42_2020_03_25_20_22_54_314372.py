palavra=str(input('Palavra:'))
lista=[]
if palavra[0]=='a':
    lista.append(palavra)
else:
    None
while not palavra=='fim':
    palavra=str(input('Palavra:'))
    if palavra[0]=='a':
        lista.append(palavra)
    else:
        None
print(lista)
