Cfim = True
while Cfim:
    palavra = str(input("digite uma palavra: "))
    lista = []
    if palavra == "fim":
        Cfim = False
    elif palavra[0] == "a":
        lista.append(palavra)
        
print(lista)