lista_com_as_palavras = []
a = input("Digite uma palavra")
while a != "fim":
    lista_com_as_palavras.append(a)
    a = input("Digite uma palavra")
i=0
while i < len(lista_com_as_palavras):
    f = lista_com_as_palavras[i]
    if f[0] == "a":
        print(f[0])
    i+=1