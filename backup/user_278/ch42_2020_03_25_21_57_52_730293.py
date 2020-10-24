lista=[]
palavras=input("Adicione palavras à lista: ")

while palavras!="fim":
    lista.append(palavras)
    palavras=input("Adicione palavras à lista: ")


i=0
while i<len(lista):
    palavra=lista[i]
    if len(palavra)>1 and palavra[0]=="a":   #len(palavra)>1 é para conferir que haja uma palavra escrita and palavra [0] se refere à primiera letra da palavra escrita
        print (palavra)
    i+=1
