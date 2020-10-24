lista = []
j = True
while j:
    palavra = input("Escolha uma plavra:")
    if palavra[0] == "a":
        lista.append(palavra)
    if palavra == "fim":
        print(lista)
        j = False