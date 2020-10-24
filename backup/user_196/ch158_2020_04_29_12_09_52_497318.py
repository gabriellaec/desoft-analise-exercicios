quantidade =0
with open("texto.txt","r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        a = linha.split(",")
        for palavra in a:
            palavra=a.split(",")
            quantidade+=1
        print(quantidade)
