x=0
lista=[]
palavra = 0
while palavra!=fim:
    palavra = input("Digite uma palavra: ")
    lista.append(palavra)
while x < len(lista):
    if (lista[x])[0] == a:
        print (lista[x])
        x+=1
    else:
        x+=1