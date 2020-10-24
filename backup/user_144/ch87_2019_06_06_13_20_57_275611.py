with open("churras.txt","r") as arquivo:
    linhas = arquivo.readlines()
    custo = 0
    qtd = 0
    preco = 0
    for i in range(len(linhas)-1):
        qtd = int(linhas[i][1])
        preco = (linhas[i][2])
        custo += qtd*preco
                
print(custo)
