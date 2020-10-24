lista=[]
palavras=input("Adicione palavras à lista: ")

while palavras!="fim":
    lista.append(palavras)
    palavras=input("Adicione palavras à lista: ")

#print (lista)

i=0
while i<len(lista):
    if lista[i][0]=="a":
        print (lista[i][0])
        i+=1
    else:
        i+=1