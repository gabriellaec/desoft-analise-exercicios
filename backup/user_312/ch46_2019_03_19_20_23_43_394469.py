lista_resposta=[]
i=0
contador=0
lista=[]
palavra = 'as palavra'
while palavra != 'fim' :
    palavra=input('escreva uma palavra ou digite "fim":')
    if palavra!='fim':
        lista.append(palavra)
while contador<len(lista):
    if lista[contador][0]=='a':
        lista_resposta.append(lista[contador])
    contador+=1
for i in lista_resposta-1:
    print(lista_resposta[i])