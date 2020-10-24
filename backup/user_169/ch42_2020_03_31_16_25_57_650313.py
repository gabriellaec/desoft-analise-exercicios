palavra=input('Escreva uma palavra ')

lista=[]

while palavra!='fim':
    if palavra[0]=='a':
        lista.append(palavra)
        palavra=input('Escreva uma palavra ')
    if palavra[0]!='a':
        palavra=input('Escreva uma palavra ')
    

