palavras = input("Digite palavras: ")
list_pal = []
while palavras != "fim":
    list_pal.append(palavras)
    palavras = input("Digite outras palavras: ")

i = 0
while i < len(list_pal):
    if list_pal[i][0] == "a":
        print(list_pal[i])
    i += 1