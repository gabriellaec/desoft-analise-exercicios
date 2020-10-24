palavra=input('Escreva uma palavra ')

lista=[]

while palavra!='fim':
    if palavra[0]=='a'and len(palavra)>1:
        lista.append(palavra)
        palavra=input('Escreva uma palavra ')
    else:
        palavra=input('Escreva uma palavra ')

