with open('churras.txt','r') as arquivo:
    linhas = arquivo.readlines()
    total = 0
    for linha in linhas:
        lista_cada_linha = linha.split(",")
        total += lista_cada_linha[1]*lista_cada_linha[2]
    print(total)
    