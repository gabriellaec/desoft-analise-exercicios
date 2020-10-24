with open("churras.txt","r",encoding = "utf8") as arquivo:
    linhas = arquivo.readlines()
    custo = 0
    qtd = 0
    preco = 0
    for i in range(len(linhas).split(","):
        qtd = int(linhas[i][1])
        preco = float(linhas[i][2])
        custo += qtd*preco
                
print(custo)
