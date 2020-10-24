lis = True
lista = []


while lis:
    palavra = str(input("Digite a palavra: "))
    if palavra [0] == "a":
        lista.append (palavra)
    elif palavra == "fim":
        lis=False
    
    
print (lista)