lista = []
x = input("palavra")
while x!="fim":
    lista.append(x)
    x = input("outra palavra")
i = 0
while i<len(lista):
    palavra = lista[i]
    if len(palavra)>1 and palavra[0] == "a":
        print(palavra[i])
        i+=1