lista_resposta=[]
contador=0
lista=[]
palavra = 'coco de gato'
while palavra != 'fim' :
    palavra=input('escreva uma palavra ou digite "fim":')
    if palavra!='fim':
        lista.append(palavra)
while contador<len(lista):
    if lista[contador][0]=='a':
        lista_resposta.append(lista[contador])
    contador+=1
contador=0
while contador<len(lista_resposta):
    print(lista_resposta[contador])
    contador+=1