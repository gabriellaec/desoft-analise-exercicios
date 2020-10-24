a = float(input("Qual é a distância que você quer percorrer em km?  "))
def calcula_preco(dist):
    if dist <= 200:
        return dist*0.50
    else:
        return 100 + dist*0.45
b = calcula_preço(a)
print("{:0.2f}".format(b))
