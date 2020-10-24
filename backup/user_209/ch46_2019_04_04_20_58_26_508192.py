def palavrobas (listeras):
    palavra = input ("Digite uma palavra: ")
    listeras = []
    while palavra != "fim":
        if palavra [0:1] == "a":
            listeras.append(palavra)
    return listeras
print(palavrobas(listeras))
            