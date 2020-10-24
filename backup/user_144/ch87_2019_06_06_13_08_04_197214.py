with open("churras.txt","r") as arquivo:
    linhas = arquivo.readlines()
    custo = 0
    qtd = 0
    preco = 0
    separando = linhas.split(",")
    qtd = int(seprando[1])
    preco = flaot(separando[2])
    custo = qtd*preco
                
print(custo)
                