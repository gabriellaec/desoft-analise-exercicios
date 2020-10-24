with open("churras.txt","r") as arquivo:
    custo = 0
    qtd = 0
    price = 0
    linhas = arquivo.readlines()
    for i in range(len(linhas.split(",")-1):
                   qnt = linhas[i][1]
                   price = linhas[i][2]
                   custo += qnt*price
   print(custo)
                  