a = input("Digite uma palavra: ")
lista=[]
i=0
while a != "fim":
    lista.append(a)
    a = input("Digite outra palavra: ")
while i<len(lista):
    a=lista[i]
    if len(a)>1 and lista[i][0]!="a":
        del(lista[i])
    else:
        print(lista[i])
    i+=1