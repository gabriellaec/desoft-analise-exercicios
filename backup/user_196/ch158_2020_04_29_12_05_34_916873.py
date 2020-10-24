with open("texto.txt","r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        a = linhas.split(",")
        print(a)
