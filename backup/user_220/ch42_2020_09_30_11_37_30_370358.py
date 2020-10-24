lista=[]
comando = True
while comando:
    pergunta=input("Escolha uma palavra: ")
    lista.append(pergunta)
    if pergunta == 'fim':
            comando = False
t=0
while t<len(lista):
    letra=lista[t]
    if letra[0] == 'a':
        print(letra)
        t+=1
    else:
        t+=1
        