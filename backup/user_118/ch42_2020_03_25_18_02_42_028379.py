lista_palavras=[]
palavras=input('Diga uma palavra: ')
while palavras != 'fim':
    lista_palavras.append(palavras)
    palavras=input('Diga uma palavra: ')
i=0
while i<len(lista_palavras):
    palavras=lista_palavras[i]
    if len(palavras)>=1 and palavras[0]=='a':
            print(palavras)
    i+=1