with open("churras.txt","r") as arquivo:
    custo = 0
    qtd = 0
    preco = 0
    linhas = arquivo.readlines()
    for i in  range(linhas.split(",")-1):
                qtd = int(linhs[i][1])
                preco = flaot(linhas[i][2])
                custo = qtd*preco
                
print(custo)
                