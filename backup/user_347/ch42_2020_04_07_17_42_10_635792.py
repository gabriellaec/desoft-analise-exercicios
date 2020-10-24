lista = []
j = True
while j:
    palavra = input("Escolha uma plavra:\n")
    if palavra[0] == "a":
        lista.append(palavra)
        print(palavra)
    if palavra == "fim":
        j = False