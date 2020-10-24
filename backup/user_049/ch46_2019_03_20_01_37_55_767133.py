lista=[]
palavra=input('Escreva uma palavra: )
while palavra != 'fim':
     lista.append(palavra)
     palavra=input('Escreve uma palavra: )
i=0
while i<len(lista):
    if lista[i][0]=='a':
        print(lista[i])
    i+=1
                   