a = input("Digite uma palavra: ")
lista=[]
i=0
while a != "fim":
    lista.append(a)
    a = input("Digite outra palavra: ")
while i<len(lista):
    a = lista[i]
    if len(a) > 1 and a[0] == "a":
        print(a)
    i+=1