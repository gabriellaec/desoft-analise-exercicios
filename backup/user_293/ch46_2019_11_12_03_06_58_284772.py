list_palavras = []
palavras = input("Digite uma palavra: ")
while palavras != "fim":
    list_palavras.append(palavras)
    palavras = input("Digite outra palavra: ")

i = 0
while i < len(list_palavras):
    palavras_list = list_palavras[i]
    if palavras_list[0] == "a":
        print(palavras_list)
    i += 1