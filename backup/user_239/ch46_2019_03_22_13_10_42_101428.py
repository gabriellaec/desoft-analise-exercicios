lista=[]
a=input('Digite uma palavra:')
while a!='fim':
    lista.append(a)
    a=input('Digite uma palavra:')

n=0

while n<len(lista):
    if lista[n][0]=='a':
        print(lista[n])
    n+=1

    
    