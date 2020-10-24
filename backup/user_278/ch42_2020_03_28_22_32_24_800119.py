lista=[]
palavras=input("Adicione palavras à lista: ")

while palavras!="fim":
    lista.append(palavras)
    palavras=input("Adicione palavras à lista: ")

i=0
while i<len(lista):
    palabra=lista[i]
    if len(palabra)>1 and palabra[0]=="a":   
        print (palabra)
        i+=1
