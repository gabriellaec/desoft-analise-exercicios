palavra = input("digite uma palavra : " )
lista = []

while palavra != "fim":
    palavra = input("digite uma palavra : " )
    if palavra[0] == "a":
        lista.append(palavra)
       
    elif palavra == "fim":
        break
print(lista)
        