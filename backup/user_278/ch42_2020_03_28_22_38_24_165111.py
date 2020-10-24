lista=[]
palavras=input("Adicione palavras à lista: ")

while palavras!="fim":
    lista.append(palavras)
    palavras=input("Adicione palavras à lista: ")

#print (lista)

i=0
while i<len(lista):
    palavra=lista[i]
    if len(palavra)>1 and palavra[0]=="a":   
        print (palavra)
    i+=1