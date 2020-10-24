with open("texto.txt","r") as arquivo:
    linhas = arquivo.readlines()
    a = linhas.split(",")
    print(a)
