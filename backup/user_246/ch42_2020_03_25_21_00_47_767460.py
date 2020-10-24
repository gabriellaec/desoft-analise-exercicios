palavra=input('Palavra:')
lista=[]
p=palavra[0]
if p=='a':
        lista.append(palavra)
else:
    None
while not palavra=='fim':
    palavra=input('Palavra:')
    p=palavra[0]
    if p=='a':
        lista.append(palavra)
    else:
        None
i=len(lista)
t=0
while t<i:
    print(lista[t])
    t+=1