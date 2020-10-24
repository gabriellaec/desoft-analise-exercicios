palavras=input('Digite uma palavra: ')
lista=[]
while palavra!='fim':
    palavra=input('Digite uma palavra: ')
    lista.append(palavra)
if palavra=='fim':
    for i in lista:
        if i[0]=='a':
            print(i)
    
    