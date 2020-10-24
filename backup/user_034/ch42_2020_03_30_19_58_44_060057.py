palavra = str(input("palavra:"))
lista = []
while palavra != "fim":
    if palavra[0] == "a":
        print (palavra)
    lista.append(palavra)
    palavra = str(input("palavra:"))
        
        