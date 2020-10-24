palavra=input('Palavra:')
lista=[]
p=palavra[0]
if p=='a':
        lista.append(palavra)
        print(lista)
else:
    print(lista)
while not palavra=='fim':
    palavra=input('Palavra:')
    p=palavra[0]
    if p=='a':
        lista.append(palavra)
        print(lista)
    else:
        print(lista)