palavra=input('Escreva uma palavra ')

lista=[]

while palavra!='fim':
        lista.append(palavra)
        palavra=input('Escreva uma palavra ')
    
i = 0
while i < len(lista):
    palavra = lista[i]
    if len(palavra) > 0 and palavra[0] == 'a':
        print(palavra)
    i += 1

