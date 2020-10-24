palavra = str(input('Qual a palavra que você deseja add a lista?'))
cont=0
contador=0
lista=[]
while palavra!='fim':
    if palavra[cont]=='a':
        lista.append(palavra)
        contador+=1
        palavra = str(input('Qual a palavra que você deseja add a lista?'))
    cont+=1
print(lista)
