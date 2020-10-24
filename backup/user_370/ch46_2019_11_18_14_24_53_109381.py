pergunta=input("Escreva uma palavra e caso queira parar digite 'fim': ")
lista_palavras=[]

while pergunta != "fim":
    lista_palavras.append(pergunta)
    pergunta=input("Escreva uma palavra e caso queira parar digite 'fim' ")
    
i=0
while i < len(lista_palavras):
    if lista_palavras[i][0] == "a":
    	print (lista_palavras[i])
    i+=1