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
    print(lista_resposta[contador])
    contador+=1
#print(lista_resposta)