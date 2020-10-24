
custo = 0
with open('churras.txt')as arquivo:
    conteudo = arquivo.readlines()
    for i in conteudo:
        quant=float(i[1])
        preco=float(i[2])
        custo+=quant*preco
        
print(custo)
 
                
