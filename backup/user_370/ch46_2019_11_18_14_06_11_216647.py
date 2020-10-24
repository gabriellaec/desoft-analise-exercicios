pergunta=input("Escreva uma palavra e caso queira parar digite 'fim': ")
lista_palavras=[]

while pergunta != "fim":
    lista_palavras.append(pergunta)
    pergunta=input("Escreva uma palavra e caso queira parar digite 'fim' ")
    
print(lista_palavras)

lista_final=[]
i=0
while i < len(lista_palavras):
    if lista_palavras[i][0] == "a":
        lista_final.append(lista_palavras[i])
    	print (lista_final)
    i+=1