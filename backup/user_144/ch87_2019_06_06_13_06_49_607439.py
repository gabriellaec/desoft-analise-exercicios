with open("churras.txt","r") as arquivo:
    custo = 0
    qtd = 0
    preco = 0
    linhas = arquivo.readlines()
    separando = linhas.split(",")
    qtd = int(seprando[1])
    preco = flaot(separando[2])
    custo = qtd*preco
                
print(custo)
                