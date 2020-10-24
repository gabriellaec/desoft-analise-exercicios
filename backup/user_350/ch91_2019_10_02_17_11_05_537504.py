with open("palavras.txt","r") as arquivo:
    contador = 0
    linhas = arquivo.readlines()
    lista_a = []
    for linha in linhas:
        dic_palavras = linha.split(",")
        for i in dic_palavras:
            if dic_palavras[0][0]=='A' or dic_palavras[0][0]=='a':
                lista_a.append(dic_palavras[0])
                
print(len(lista_a))