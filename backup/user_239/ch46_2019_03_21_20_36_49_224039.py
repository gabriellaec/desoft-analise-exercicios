lista=[]
a=input('Digite uma palavra:')
while a!='fim':
    lista.append(a)
    a=input('Digite uma palavra:')

print('Palavras da lista:')
print(lista)

n=0

while n<len(lista):
    if lista[n][0]!='a':
        del lista[n]
    n+=1
print('Palavras apenas com a letra a:')
print(lista)
    